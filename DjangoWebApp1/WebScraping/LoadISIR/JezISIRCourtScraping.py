# https://www.dataquest.io/blog/web-scraping-tutorial-python/

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


import requests
from bs4 import BeautifulSoup



class IsirCourtClass(object):
# This class serves to connect to ISIR web page and scrape atributes of to which court the case belongs

    def __init__(self, code_ins_case):
        self.codeInsCase = code_ins_case  # string like "12345/2018" expected
        self.idInsCase = code_ins_case.split('/')[0]
        self.yearInsCase = code_ins_case.split('/')[1]
        page_url = "https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?nazev_osoby=&jmeno_osoby=&ic=&datum_narozeni=&rc=&mesto=&cislo_senatu=" + "&bc_vec=" + self.idInsCase + "&rocnik=" + self.yearInsCase + "&id_osoby_puvodce=&druh_stav_konkursu=&datum_stav_od=&datum_stav_do=&aktualnost=AKTUALNI_I_UKONCENA&druh_kod_udalost=&datum_akce_od=&datum_akce_do=&nazev_osoby_f=&cislo_senatu_vsns=&druh_vec_vsns=&bc_vec_vsns=&rocnik_vsns=&cislo_senatu_icm=&bc_vec_icm=&rocnik_icm=&rowsAtOnce=50&captcha_answer=&spis_znacky_datum=&spis_znacky_obdobi=14DNI"

        self._get_isir_request(page_url)

        self._get_court()

    def _get_isir_request(self, page_url):
        self.page = requests.get(page_url, timeout=10)

        # 200 is code for ok request result, otherwise raise exception
        assert(self.page.status_code == 200), "JEZ-8671143: Request failed with status_code = " + str(self.page.status_code)

    def _get_court(self):
        # Parse the html
        soup = BeautifulSoup(self.page.content, 'html.parser')
        class_name = 'vysledekLustrace'
        results = soup.findAll('span', {'class': class_name})

        try:
            self.courtCode = results[0].get_text().strip()[0:4]  # the code is hidden in the first for letters
            self.courtFullNameRaw = results[1].get_text().strip()  # this is saved in 2nd grammatical case - genitiv - needs to be adjusted afterwards
            self.courtFullName = self._get_full_court_name(self.courtCode)

        except:
            print("JEZ-78616: Error when parsing " + class_name + "INS: " + str(self.codeInsCase))

    def append_results_to_file(self, file_path):
        new_row = "\n" + self.codeInsCase + ";" + self.courtCode + ";" + self.courtFullName + ";" + self.courtFullNameRaw

        with open(file_path, 'a') as fd:
            fd.write(new_row)
            
    def _get_full_court_name(self,courtCode):

        courtdict = {
            "KSOL": "Krajský soud v Ostravě - pobočka v Olomouci",
            "KSBR": "Krajský soud v Brně",
            "KSCB": "Krajský soud v Českých Budějovicích",
            "KSUL": "Krajský soud v Ústí nad Labem",
            "KSLB": "Krajský soud v Ústí nad Labem - pobočka v Liberci",
            "KSOS": "Krajský soud v Ostravě",
            "KSPH": "Krajský soud v Praze",
            "KSHK": "Krajský soud v Hradci Králové",
            "KSPA": "Krajský soud v Hradci Králové - pobočka v Pardubicích",
            "KSPL": "Krajský soud v Plzni",
            "MSPH": "Městský soud v Praze",

        # more to come
        }

        if courtCode in courtdict:
            return courtdict[courtCode]
        else:
            print("Court code not found in dictionary")
            return "N/A"

    def main(self):
        pass


# isir = IsirCourtClass("18014/2018")
# isir = IsirCourtClass("17968/2018")
# isir = IsirCourtClass("19606/2018")
# isir = IsirCourtClass("9999/2018")
# isir = IsirCourtClass("9494/2018") # test case for RISK-1383
#
#
# isir.courtCode
# isir.courtFullName
# isir.courtFullNameRaw

