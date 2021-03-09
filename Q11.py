import requests
import math

exchangeRateUrl = 'https://api.exchangerate-api.com/v4/latest/TWD'  #以TWD為基準
exchangeRateData = requests.get(exchangeRateUrl)
exchangeRateTable = exchangeRateData.json()
print('USD : '+str(exchangeRateTable['rates']['USD']))
print('JPY : '+str(exchangeRateTable['rates']['JPY']))
print('EUR : '+str(exchangeRateTable['rates']['EUR']))
print('GBP : '+str(exchangeRateTable['rates']['GBP']))

moneyFrom = float(input('How many TWD are you exchanging? '))
country = input('Which country do you want to exchange? ')

rate = exchangeRateTable['rates'][country]
moneyTo = math.ceil(moneyFrom*rate*1)/1.0


print(f'{moneyFrom} TWD at an exchange rate of {rate} is {moneyTo} {country} dollars.')