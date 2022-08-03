from time import clock_settime
import requests
from pathlib import Path
import re, csv

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=RRIW0YM0PRPMKD9Q'
response = requests.get(url)
data = response.json()
print(data)

file_path2 = Path.cwd()/"TeamB"/"summary_report.txt"
file_path2.touch()
print(file_path2.exists())

file_path2.touch()

print(data["5. Exchange Rate"])

if file_path2.exists():
    with file_path2.open('w', encoding = 'UTF-8', newline = '') as file:
        writer = csv.writer(file)
        for item in data.values():
            writer.writerow([item["5. Exchange Rate"]])



