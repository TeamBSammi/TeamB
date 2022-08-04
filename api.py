import requests
from pathlib import Path
import re, csv

# setting api key
apikey = 'RRIW0YM0PRPMKD9Q'
# inserting api key to url and setting as url
url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={apikey}'
# request access to url and assign it as response
response = requests.get(url)
# retrieve data with .json from response and save it as data
data = response.json()
# setting filepath
fp = Path.cwd()/'summary_report.txt'


for item in data.values():
    # converting data to float and assigning it as forex
    forex = float(data['Realtime Currency Exchange Rate']["5. Exchange Rate"])

# defining a function named api_function()
def api_function():
    # continue running if file path exists
    if fp.exists():
        # opening a new file and append in it
        with fp.open(mode ="a", encoding = "utf-8",newline = "") as file:
            # writing line with forex data
            file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] US$1 = {forex}\n")

api_function()
