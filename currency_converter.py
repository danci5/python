#currencyconverter-myfirstcontribution

import requests

amount = float(raw_input('amount: '))

input_currency = raw_input('input currency: ')

output_currency = raw_input('output currency: ')

if not output_currency:

    currencies = ["ARS","USD","AUD","BTC","BRL","CAD","CLP","CNY","CZK","DKK","EUR","FJD","HNL","HKD","HUF",
                    "ISK","INR","IDR","ILS","JPY","KRW","MYR","MXN","NZD","NOK","PKR","PHP","PLN","RUB","SGD",
                    "ZAR","SEK","CHF","TWD","THB","TRY","GBP","USD","VND"]
    
    for i in currencies:
        url = ('https://currency-api.appspot.com/api/%s/%s.json') % (input_currency, i)
        r = requests.get(url)
        
        print i,amount*float(r.json()['rate'])
else:

    url = ('https://currency-api.appspot.com/api/%s/%s.json') % (input_currency, output_currency)
    r = requests.get(url)

    print
    print output_currency,amount*float(r.json()['rate'])


