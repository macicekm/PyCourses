
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

import logging

# Set global parameters
logging.basicConfig(filename='get_PM_decisions.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
dtime_start = datetime.datetime.now()
path_to_driver = 'D:\\Users\\mmacicek1695ab\\PycharmProjects\\PyCourses\\DjangoWebApp1\\WebScraping\\Justice\\chromedriver'


# Get clients
path_to_csv = "D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\FilesFromJustice\\collection_cases.csv"

with open(path_to_csv) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    cc_dict = {}

    for row in reader:
        cc_dict[row['COLLECTION_CASE']] = row['FOLDER_NAME']


# Set class
class InfoDocumentClass(object):
# This class serves to connect to infodokument.justice web page, get the info whether we have PM decision or not and download pdf document
# Web site does not accept POST request, so we need to use selenium to operate it

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
        browser.minimize_window()

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

class NullPDFTextError(Exception):
    pass


for cc in tqdm(cc_dict):

    print('Current collection case: ' + cc + ' folder: ' + cc_dict[cc])
    document = InfoDocumentClass(cc)
    document.get_documents()


##############################################################################################################################################################
print("Finished, time elapsed = " + str(round((datetime.datetime.now() -dtime_start).total_seconds()/60, 2)) + " minutes")