# https://infodokument.justice.cz/

# https://www.youtube.com/watch?v=GJjMjB3rkJM&feature=youtu.be  # tutorial video


###
# from link on https://www.seleniumhq.org/ you need to download a webdriver
# for chrome go directly here https://sites.google.com/a/chromium.org/chromedriver/ and install it somewhere on your PC

# install selenium and pywget using Anaconda
# install slate3k using pip -- not in anaconda distribution
# As of now, this script does not work when being connected to NASE_SIT, so be connected to PRIPOJENI_DO_SVETA


# import cx_Oracle


import slate3k as slate
# import PyPDF2

from selenium import webdriver
import wget
# from selenium.webdriver.common.keys import Keys # useful if you want to press keyboard buttons like enter

import datetime
import time



# To Do Database connection - does not work yet

# password = input("Zadej heslo do DB")
# con = cx_Oracle.connect('mmacicek1695ab/' + password + '@HDWMN.BANKA.HCI/orcl')
# print con.version
# con.close()


# TO DO
# For logging use python logging package


# Set global parameters
dtime_start = datetime.datetime.now()
url = "https://infodokument.justice.cz/"
path_to_driver = 'D:\\Users\\mmacicek1695ab\\PycharmProjects\\PyCourses\\DjangoWebApp1\\WebScraping\\Justice\\chromedriver'
path_to_save_file = 'D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\FilesFromJustice'
path_to_neepr_file = 'D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\FilesFromJustice' + '\\NePM EPR.pdf'
page_url = "https://infodokument.justice.cz"


# PyPDF2 Does not work - imports empty string
    # pdfFileObj = open(path_to_neepr_file, 'rb')
    # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # pdfReader.numPages
    # pageObj = pdfReader.getPage(1)
    # text = pageObj.extractText()
    # print(text)


# Open PDF and get identificators
with open(path_to_neepr_file,'rb') as f:
    text = str(slate.PDF(f))
print(text)

spis_rocnik = text[text.find('EPR\\xa0')+7:text.find('\\xa0-\\xa07')].split('/')

spec_ident = text[text.find('Specifický identifikátor: ')+26:text.find('Specifický identifikátor: ')+26+23]

dict_justice = {
    "overovaciKod": spec_ident,
    "spznBc": spis_rocnik[0],
    "spznRocnik": spis_rocnik[1]
}


# Open browser
browser = webdriver.Chrome(path_to_driver)

# Insert web Page
browser.get(page_url)

# Get elements
elem_overovaciKod = browser.find_element_by_id('overovaciKod')
elem_spisovka = browser.find_element_by_id('spznBc')
elem_rocnik = browser.find_element_by_id('spznRocnik')
elem_button_find = browser.find_elements_by_xpath("//*[contains(text(), 'Vyhledat dokument')]")[0] # returns originally a list of elements
elem_button_clear = browser.find_elements_by_xpath("//*[contains(text(), 'Vyčistit formulář')]")[0]

# elem.send_keys(Keys.Enter)

# Insert identeficators into inputboxes
elem_overovaciKod.clear()  # needs to be cleared first
elem_overovaciKod.send_keys(dict_justice["overovaciKod"])
elem_spisovka.clear()  # needs to be cleared first
elem_spisovka.send_keys(dict_justice["spznBc"])
elem_rocnik.clear()  # needs to be cleared first
elem_rocnik.send_keys(dict_justice["spznRocnik"])

# Click find button to find related PDFs links
elem_button_find.click()

#elem_just = browser.find_element_by_class_name('just')

# Wait for 1 second - give the server time to find the documents
time.sleep(1)

# Download pdf page if there is any
try:
    elem_pm_rozhodnuti = browser.find_elements_by_xpath("//*[contains(text(), 'Pravomocné rozhodnutí.pdf')]")[0]
except:
    print('PM not found')
else:
    # download pm_rozhodnuti
    print('PM found and will be downloaded')
    wget.download(elem_pm_rozhodnuti.get_attribute('href'), path_to_save_file + '\\pm_rozhodnuti.pdf')

browser.close()

##############################################################################################################################################################
print("Finished, time elapsed = " + str(round((datetime.datetime.now() -dtime_start).total_seconds()/60, 2)) + " minutes")


#############################
# OLD CODE ##################
#############################

# https://stackoverflow.com/questions/1555234/fill-form-values-in-a-web-page-via-a-python-script-not-testing
# http://wwwsearch.sourceforge.net/mechanize/download.html

# import requests
# from bs4 import BeautifulSoup
#
#
#
# page = requests.get(page_url, timeout=10)
#
# # Parse the html
# soup = BeautifulSoup(page.content, 'html.parser')
# id = 'overovaciKod'
# results = soup.findAll()


# import re
# from mechanize import Browser
#
# br = Browser()
# br.open("http://www.example.com/")
# br.select_form(name="order")
# # Browser passes through unknown attributes (including methods)
# # to the selected HTMLForm (from ClientForm).
# br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)
# response = br.submit()  # submit current form


# https://dzone.com/articles/how-submit-web-form-python
#import requests

# payload = {'overovaciKod':overovaci_kod
#            ,'spznBc':spisovka
#            ,'spznRocnik':rocnik
# }
# r = requests.post(url, payload)
# print(r.content)


# this page does not submit post requests -- aarrgghh
