
# https://infodokument.justice.cz/
# http://infosoud.justice.cz/

# import cx_Oracle


import slate3k as slate

from selenium import webdriver
import wget
# from selenium.webdriver.common.keys import Keys # useful if you want to press keyboard buttons like enter

import datetime
import time
import csv
import os
from tqdm import tqdm  # progress bar in console
import random

import logging

import requests
from bs4 import BeautifulSoup
import re
import cx_Oracle
import pandas as pd



# Set global parameters
logging.basicConfig(filename='get_PM_decisions.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
dtime_start = datetime.datetime.now()
path_to_driver = 'D:\\Users\\mmacicek1695ab\\PycharmProjects\\PyCourses\\DjangoWebApp1\\WebScraping\\Justice\\chromedriver'
schema = 'APP_COLL_JEZEVCIK_TEST'


# Connection to Oracle Class

class ABOracleConnClass(object):
    def __init__(self, server, username):
        """ initialize connection class
        :param server: name of the server to connect to
        :param username: login username
        """
        def get_password(f_list):

            import os

            for file in f_list:
                if os.path.exists(file):
                    f = open(file, "r")
                    res = f.readline().split(';')
                    if res[0] == username:
                        return res[1]
                    else: input("Insert password")

        services_dict = {
            'PROD': {'host': 'DBHDWMN.BANKA.HCI', 'port': 1521, 'service': 'HDWMN.BANKA.HCI'},
            'PREPROD': {'host': 'UF-SX06.BANKA.HCI', 'port': 1521, 'service': 'MNPPDW.BANKA.HCI'}
        }

        password_files_list = ["D:\\Users\\" + username + "\\Documents\\Jezevčík\\secret.txt",
                               "C:\\Users\\" + username + "\\Documents\\Jezevčík\\secret.txt",
                               "D:\\Users\\" + username + "\\Documents\\Uw_debt_report\\secret.txt",
                               "C:\\Users\\" + username + "\\Documents\\Uw_debt_report\\secret.txt",
        ]


        password = get_password(password_files_list)


        conn_info = {
            'host': services_dict[server]['host'],
            'port': services_dict[server]['port'],
            'user': username,
            'psw': password,
            'service': services_dict[server]['service'],
        }

        self.conn_str = '{user}/{psw}@{host}:{port}/{service}'.format(**conn_info)

    def con(self):
        """ function returns connection to oracleDB
        :return: Connection object
        """
        return cx_Oracle.connect(self.conn_str)




# Set class
class InfoDocumentClass(object):
    # This class serves to connect to infodokument.justice web page, get the info whether we have PM decision or not and download pdf document
    # Web site does not accept POST request, so we need to use selenium to operate it

    # To Do: for some reason i am unable to scrape identifiers from pdf... -> it returns empty text

    def __init__(self, id_collection_case):

        self.id_collection_case = id_collection_case
        self.page_url = "https://infodokument.justice.cz"
        self.folder_path = self._get_clients_folder_path()
        self.process_ids = self._get_process_ids()

    def _get_clients_folder_path(self):

        folder_path = 'D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\FilesFromJustice\\' + cc_dict[str(self.id_collection_case)]
        if os.path.exists(folder_path):
            return folder_path
        else:
            logging.error('%s raised an error: Folder path does not exist ', folder_path)

    def _get_process_ids(self):
        # Open PDF and get identificators - store it in a dictionary
        try:
            with open(self.folder_path + '\\NePM EPR.pdf', 'rb') as f:
                text = str(slate.PDF(f))

            if text == '[]':
                raise NullPDFTextError

            spis_rocnik = text[text.find('EPR\\xa0') + 7:text.find('\\xa0-')].split('/')

            spec_ident = text[
                         text.find('Specifický identifikátor: ') + 26:text.find('Specifický identifikátor: ') + 26 + 23]

        except NullPDFTextError:
            logging.error('%s raised an error: Unable to read identifiers from pdf ', self.folder_path + '\\NePM EPR.pdf')

            return {
                "overovaciKod": "",
                "spznBc": "0",
                "spznRocnik": "1900"
            }

        except:
            logging.error('%s raised an error: General error when reading identifiers from PDF ', self.id_collection_case)

            return {
                "overovaciKod": "",
                "spznBc": "0",
                "spznRocnik": "1900"
            }

        else:
            return {
                "overovaciKod": spec_ident,
                "spznBc": spis_rocnik[0],
                "spznRocnik": spis_rocnik[1]
            }

    def get_documents(self):
        # This method downloads document with PM pdf


        # Open browser if not already opened
        browser = webdriver.Chrome(path_to_driver)
        # browser.minimize_window()

        # Insert web Page
        browser.get(self.page_url)

        # Get elements
        elem_overovaciKod = browser.find_element_by_id('overovaciKod')
        elem_spisovka = browser.find_element_by_id('spznBc')
        elem_rocnik = browser.find_element_by_id('spznRocnik')
        elem_button_find = browser.find_elements_by_xpath("//*[contains(text(), 'Vyhledat dokument')]")[
            0]  # returns originally a list of elements
        # elem_button_clear = browser.find_elements_by_xpath("//*[contains(text(), 'Vyčistit formulář')]")[0]

        # elem.send_keys(Keys.Enter)

        # Insert identificators into inputboxes
        elem_overovaciKod.clear()  # needs to be cleared first
        elem_overovaciKod.send_keys(self.process_ids["overovaciKod"])
        elem_spisovka.clear()  # needs to be cleared first
        elem_spisovka.send_keys(self.process_ids["spznBc"])
        elem_rocnik.clear()  # needs to be cleared first
        elem_rocnik.send_keys(self.process_ids["spznRocnik"])

        # Click find button to find related PDFs links
        elem_button_find.click()

        # elem_just = browser.find_element_by_class_name('just')

        # Wait for 1 second - give the server time to find the documents
        time.sleep(1)

        # Download pdf page if there is any
        try:
            elem_pm_rozhodnuti = browser.find_elements_by_xpath("//*[contains(text(), 'Pravomocné rozhodnutí.pdf')]")[0]
        except:
            print('PM not found CC: ' + self.id_collection_case)
            logging.info('%s info: PM not found for CC:', self.id_collection_case)
        else:
            # download pm_rozhodnuti
            wget.download(elem_pm_rozhodnuti.get_attribute('href'), self.folder_path + '\\pm_rozhodnuti.pdf')
            print('PM found and downloaded CC: ' + self.id_collection_case)
            logging.info('%s info: PM found and downloaded for CC:', self.id_collection_case)

        browser.close()

# This class is used when raising an error in InfoDocumentClass._get_process_ids()
class NullPDFTextError(Exception):
    pass


# Set class
class InfoSoudClass(object):
    # This class serves to connect to infodokument.justice web page, get the info whether we have PM decision or not and download pdf document
    # Web site does not accept POST request, so we need to use selenium to operate it

    # To Do: for some reason i am unable to scrape identifiers from pdf... -> it returns empty text

    def __init__(self, id_collection_case):

        self.id_collection_case = id_collection_case

        self.folder_path = self._get_clients_folder_path()
        self.process_ids = self._get_process_ids()
        self.page_url = "http://infosoud.justice.cz/InfoSoud/public/search.do;" \
                        "jsessionid=" + self.process_ids["sessionId"] + \
                        ".infosoud01?type=spzn&typSoudu=os&" \
                        "krajOrg=" + self.process_ids["krajOrg"] + \
                        "&org=" + self.process_ids["org"] + \
                        "&cisloSenatu=" + self.process_ids["cisloSenatu"] + \
                        "&druhVec=" + self.process_ids["druhVec"] + \
                        "&bcVec=" + self.process_ids["bcVec"] + \
                        "&rocnik=" + self.process_ids["rocnik"] + \
                        "&spamQuestion=23&agendaNc=CIVIL"

    def _get_clients_folder_path(self):

        folder_path = 'D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\FilesFromJustice\\' + cc_dict[str(self.id_collection_case)]
        if os.path.exists(folder_path):
            return folder_path
        else:
            logging.error('%s raised an error: Folder path does not exist ', folder_path)

    def _get_process_ids(self):
        # Get identificators - store it in a dictionary

        return {
            "sessionId": str(random.randint(1,100000)),  # clicking on search button generates some sessionID - since I don´t have this I generate some random number
            "krajOrg": "KSSTCAB",
            "org": "OSSTCPY",
            "cisloSenatu": "21",
            "druhVec": "C",
            "bcVec": "10",
            "rocnik": "2018"
        }

    def is_pm_info(self):
        # Get the information from the website, whether we already have PM decision or not
        page = requests.get(self.page_url, timeout=10)

        # 200 is code for ok request result, otherwise raise exception
        assert(page.status_code == 200), "JEZ-1789116: Request failed with status_code = " + str(page.status_code)

        # Parse the html
        soup = BeautifulSoup(page.content, 'html.parser')
        # id_pm = "udalost15" + self.process_ids["org"] + self.process_ids["druhVec"] + self.process_ids["rocnik"] + self.process_ids["cisloSenatu"] + self.process_ids["bcVec"]
        # result = soup.find("a", {"id": id_pm})
        result = soup.find("a", text=re.compile(".*Datum pravomocného ukončení věci.*"))  # Text is stored with lots of spaces, its not possible to find it by id since it changes

        if not result is None:
            return True
        else:
            return False

        # Wait for 3 seconds - make it look more like a human behind his laptop
        time.sleep(3)

########################################################################################################################
# This is the real executable code
########################################################################################################################


# Get clients
sql = """
      SELECT ID_COLLECTION_CASE, NAME||' '||CUID||' CC'||ID_COLLECTION_CASE AS FOLDER_NAME
      from collection_case cc
      JOIN person p ON cc.id_person = p.id_person
      AND cc.flag_deleted = 'N' AND cc.flag_collected = 'Y'
      WHERE mod(id_collection_case,500) = 0
      """
con = ABOracleConnClass('PROD', 'MMACICEK1695AB')
df = pd.read_sql(sql, con=con.con())
cc_dict = df.set_index('ID_COLLECTION_CASE')['FOLDER_NAME'].to_dict()

con.close()


# Infosoud
if False:
    info_soud = InfoSoudClass("55")
    print(info_soud.is_pm_info())

# Infodokument Justice
if True:
    for cc in tqdm(cc_dict):

        print('Current collection case: ' + cc + ' folder: ' + cc_dict[cc])
        info_document = InfoDocumentClass(cc)
        info_document.get_documents()


########################################################################################################################
print("Finished, time elapsed = " + str(round((datetime.datetime.now() - dtime_start).total_seconds()/60, 2)) + " minutes")


