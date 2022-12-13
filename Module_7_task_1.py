from bs4 import BeautifulSoup
import requests

page = requests.get('https://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text,'html.parser')
table = soup.find('table',{'class':'mfd-table mfd-currency-table'})

usd_rate = table.find_all('td')
result = [usd.text for usd in usd_rate]

for i in range(0, len(result)-2, 3):
   print('Date:'+ result[i] + ' USD_rate: ' + result[i+1] + ' Change --> ' + result[i+2])


