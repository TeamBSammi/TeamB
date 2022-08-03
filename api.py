
import requests
from pathlib import Path
import re, csv

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=RRIW0YM0PRPMKD9Q'
response = requests.get(url)
data = response.json()
print(data)

for item in data.values():
    rate = (item["5. Exchange Rate"])

print(rate)

txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

with txtfile.open(mode = "w",encoding = "utf-8",newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(f"[CURRENCY CONVERSION RATE] US$1 = {rate}")




