import requests
from pathlib import Path
import re, csv

apikey = 'RRIW0YM0PRPMKD9Q'
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={apikey}'
response = requests.get(url)
data = response.json()
fp = Path.cwd()/'summary_report.txt'

for item in data.values():
    forex = float(data['Realtime Currency Exchange Rate']["5. Exchange Rate"])

def api_function():
    if fp.exists():
        with fp.open(mode ="a", encoding = "utf-8",newline = "") as file:
            file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] US$1 = {forex}\n")

api_function()

#for item in data.values():
    #rate = (item["5. Exchange Rate"])

#apirate = float(rate)

#txtfile = Path.cwd()/"summary_report.txt"
#txtfile.touch()

#with txtfile.open(mode = "w",encoding = "utf-8",newline = "") as file:
#    file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] US$1 = {rate}")




