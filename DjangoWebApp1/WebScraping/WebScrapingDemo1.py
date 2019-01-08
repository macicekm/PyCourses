# https://www.dataquest.io/blog/web-scraping-tutorial-python/


# https://www.linode.com/docs/applications/big-data/how-to-scrape-a-website-with-beautiful-soup/
    # featuring some automated daily job


"""
https://isir.justice.cz/isir/common/stat.do?kodStranky=PROVOZPODMINKY

Účelem provozování aplikace je zveřejňování veškerých relevantních informací týkajících se insolvenčních správců,
dokumentů z insolvenčních spisů i zákonem stanovených informací týkajících se dlužníků.
K tomuto účelu není pro běžného uživatele přístup k informacím na WWW serveru omezen.
S ohledem na tento charakter provozu WWW serveru a na jeho zabezpečení si proto Ministerstvo spravedlnosti vyhrazuje právo omezit
či zakázat přístup k databázi insolvenčního rejstříku uživateli, který denně
odešle k vyřízení více než 3000 požadavků a/nebo se snaží o překročení ochrany tohoto
WWW serveru a/nebo který odešle k vyřízení více než 50 požadavků během jedné (1) minuty.
"""

# there is a problem, that requests.get is not available when connected to air bank internal WI-FI
# due to that reason you must switch to NASE_SIT - however, then you loose other connections to local network


"""to do:

>> Add error handler for request fail
>> Add waiting time to simulate 'real user' request
>> Add timeout
>> Save results
>> Load data, prepare loop and save data
>> Define subset of insolvency cases entering the program
>> Automate program

"""

from DjangoWebApp1.WebScraping.LoadISIR.JezISIRCourtScraping import IsirCourtClass
from time import sleep
import csv

with open('D:/Users/mmacicek1695ab/PycharmProjects/PyCourses/insTestCases.csv', 'r') as f:
    reader = csv.reader(f)
    insTestList = list(reader)


for insCase in insTestList:
    str_insCase = str.replace(str.replace(str(insCase),"['",""),"']","")
    isir = IsirCourtClass(str_insCase)

    isir.append_results_to_file('D:/Users/mmacicek1695ab/PycharmProjects/PyCourses/isirCourtResults.csv')

    sleep(3)  # freeze program for 5 seconds to simulate human-like behavior

    print(str_insCase + " Done")




#
# import requests
# from bs4 import BeautifulSoup
#
#
# codeInsCase = "17968/2018"
#
# idSpis = codeInsCase.split('/')[0]
# rok = codeInsCase.split('/')[1]
#
# pageURL = "https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?nazev_osoby=&jmeno_osoby=&ic=&datum_narozeni=&rc=&mesto=&cislo_senatu=" + "&bc_vec=" + idSpis + "&rocnik=" + rok + "&id_osoby_puvodce=&druh_stav_konkursu=&datum_stav_od=&datum_stav_do=&aktualnost=AKTUALNI_I_UKONCENA&druh_kod_udalost=&datum_akce_od=&datum_akce_do=&nazev_osoby_f=&cislo_senatu_vsns=&druh_vec_vsns=&bc_vec_vsns=&rocnik_vsns=&cislo_senatu_icm=&bc_vec_icm=&rocnik_icm=&rowsAtOnce=50&captcha_answer=&spis_znacky_datum=&spis_znacky_obdobi=14DNI"
#
# page = requests.get(pageURL)
# # prints reponse object
# print(page)
#
# # prints status
# # A status_code of 200 means that the page was downloaded successfully
# # status_code 502 - nedostupný
# print(page.status_code)
#
# # print downloaded html
# print(page.content)
#
# # Parse the html
# soup = BeautifulSoup(page.content, 'html.parser')
#
# print(soup.prettify())
#
#
# list(soup.children)
#
# soup.find_all(class_='vysledekLustrace')
#
# soup.find_all('i', class_='vysledekLustrace')
# soup.find_all('i', class_='vysledekLustrace')[0].get_text()
#
#
# results = soup.findAll('span', {'class' :'vysledekLustrace'})
#
# resCourtCode = results[0].get_text().strip()[0:4] # the code is hidden in the first for letters
# resCourtFullName = results[1].get_text().strip() # this is save in 2.case - genitiv - needs to be adjusted afterwards
#
# print(resCourtCode)
#
# print(resCourtFullName)






