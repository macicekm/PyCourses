# https://infodokument.justice.cz/

# https://www.youtube.com/watch?v=GJjMjB3rkJM&feature=youtu.be  # tutorial video



# from link on https://www.seleniumhq.org/ you need to download a webdriver
# for chrome go directly here https://sites.google.com/a/chromium.org/chromedriver/ and install it somewhere on your PC

# install selenium and pywget using Anaconda

from selenium import webdriver
import wget
# from selenium.webdriver.common.keys import Keys # useful if you want to press keyboard buttons like enter


url = "https://infodokument.justice.cz/"


dict_justice = {
    "overovaciKod" : "3GA7L-D89EO-RYN6D-JG1ST",
    "spznBc" : "212882",
    "spznRocnik" : "2018"
}

# dict_justice = {
#     "overovaciKod" : "3YSDI-SG614-UW8B1-MQ3IP",
#     "spznBc" : "296674",
#     "spznRocnik" : "2018"
# }

path_to_driver = 'D:\\Users\\mmacicek1695ab\\PycharmProjects\\PyCourses\\DjangoWebApp1\\WebScraping\\Justice\\chromedriver'
page_url = "https://infodokument.justice.cz"

browser = webdriver.Chrome(path_to_driver)

browser.get(page_url)

elem_overovaciKod = browser.find_element_by_id('overovaciKod')
elem_spisovka = browser.find_element_by_id('spznBc')
elem_rocnik = browser.find_element_by_id('spznRocnik')
elem_button_find = browser.find_elements_by_xpath("//*[contains(text(), 'Vyhledat dokument')]")[0] # returns originally a list of elements
elem_button_clear = browser.find_elements_by_xpath("//*[contains(text(), 'Vyčistit formulář')]")[0]

# elem.send_keys(Keys.Enter)

elem_overovaciKod.send_keys(dict_justice["overovaciKod"])
elem_spisovka.send_keys(dict_justice["spznBc"])
elem_rocnik.clear() # needs to be cleared first
elem_rocnik.send_keys(dict_justice["spznRocnik"])

elem_button_find.click()

elem_just = browser.find_element_by_class_name('just')

elem_rozhodnuti = browser.find_elements_by_xpath("//*[contains(text(), 'Rozhodnutí.pdf')]")[0]
elem_pm_rozhodnuti = browser.find_elements_by_xpath("//*[contains(text(), 'Pravomocné rozhodnutí.pdf')]")[0]



print(elem_just.text)
print(elem_rozhodnuti.get_attribute('href'))
print(elem_pm_rozhodnuti.get_attribute('href'))





print('Beginning file download with wget module')
# download rozhodnuti
wget.download(elem_rozhodnuti.get_attribute('href'), 'D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\FilesFromJustice\\rozhodnuti.pdf')
# download pm_rozhodnuti
wget.download(elem_pm_rozhodnuti.get_attribute('href'), 'D:\\Users\\mmacicek1695ab\\Desktop\\Work\\Tasks\\GITProjects\\test\\FilesFromJustice\\pm_rozhodnuti.pdf')




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
