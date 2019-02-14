#  https://currencylayer.com

import requests

api = '672e7a74ebe05b6a92a63bf5a19babbe'

params = {'access_key': api, 'format': 1}

r = requests.get('http://apilayer.net/api/live', params = params)

livequote = r.json()

print('Insert currencies for which you\'d like to get exchange rate')
curr1 = input('Currency one: ')
curr2 = input('Currency two: ')

try:
    ex_rate1 = livequote['quotes']['USD'+curr1]
    ex_rate2 = livequote['quotes']['USD'+curr2]

    print('Exchange rate of currencies ' + curr1 + '/' + curr2 + ' is: ' + str(ex_rate1 / ex_rate2))
except:
    print('Unable to find requested currency code')

