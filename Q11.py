import requests
import math

def roundUp(num, dig):
    digNum = math.pow(10, dig)
    return math.ceil(num*digNum)/digNum

minCurrencyUnit={
    'USD':2,
    'JPY':0,
    'EUR':2,
    'GBP':2

}
exchangeRateUrl = 'https://api.exchangerate-api.com/v4/latest/TWD'  #以TWD為基準
exchangeRateData = requests.get(exchangeRateUrl)
exchangeRateTable = exchangeRateData.json()
print('USD : '+str(exchangeRateTable['rates']['USD']))
print('JPY : '+str(exchangeRateTable['rates']['JPY']))
print('EUR : '+str(exchangeRateTable['rates']['EUR']))
print('GBP : '+str(exchangeRateTable['rates']['GBP']))

moneyFrom = float(input('How many TWD are you exchanging? '))
currency = input('Which currency do you want to exchange? ')

rate = exchangeRateTable['rates'][currency]
moneyTo = roundUp(moneyFrom*rate, minCurrencyUnit[currency])


print(f'{moneyFrom} TWD at an exchange rate of {rate} is {moneyTo} {currency} dollars.')