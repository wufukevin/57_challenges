import requests
import math

url = 'https://api.exchangerate-api.com/v4/latest/TWD'  #以TWD為基準
res = requests.get(url)
data = res.json()
print('USD : '+str(data['rates']['USD']))
print('JPY : '+str(data['rates']['JPY']))
print('EUR : '+str(data['rates']['EUR']))
print('GBP : '+str(data['rates']['GBP']))

moneyFrom = float(input('How many TWD are you exchanging? '))
country = input('Which country do you want to exchange? ')

rate = data['rates'][country]
moneyTo = math.ceil(moneyFrom*rate*1)/1.0


print(str(moneyFrom)+' TWD at an exchange rate of '+str(rate)+' is '+str(moneyTo)+country+' dollars.')