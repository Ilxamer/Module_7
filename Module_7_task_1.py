from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

url = "http://mfd.ru/currency/?currency=USD"
page = requests.get(url)
dollars = []
search = []
x = []
y = []

soup = BeautifulSoup(page.text, "html.parser")
search = soup.findAll(class_="mfd-table mfd-currency-table")

for data in search:
    if data.find_all(class_="mfd-table mfd-currency-table") is not None:
        dollars.append(data.text)

elements = []

for data in dollars:
    elements = str(data).split()

len1 = len(elements)

for i in range(len1 - 1, 3, -4):
    x.append(str(elements[i - 2]))
    y.append(float(str(elements[i - 1])))

fig, ax = plt.subplots()

ax.plot(x, y)
ax.set(title='Курс доллара к рублю', xlabel='Дата', ylabel='Курс')
ax.xaxis.set_major_locator(MaxNLocator(4))
ax.grid(True)
plt.show()