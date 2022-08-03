
import requests
from pathlib import Path
import re, csv

apikey = 'RRIW0YM0PRPMKD9Q'
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={apikey}}'
response = requests.get(url)
data = response.json()
fp = Path.cwd()/'summary_report.txt'

def api_function():
    for item in data.values():
        forex = (item["5. Exchange Rate"])
        forex = float(forex)
    if fp.exists():
        with fp.open(mode = "w",encoding = "utf-8",newline = "") as file:
           file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] US$1 = {forex}")
    return forex

#for item in data.values():
    #rate = (item["5. Exchange Rate"])

#apirate = float(rate)

#txtfile = Path.cwd()/"summary_report.txt"
#txtfile.touch()

#with txtfile.open(mode = "w",encoding = "utf-8",newline = "") as file:
#    file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] US$1 = {rate}")




