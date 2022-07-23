
import requests
from pathlib import Path
import csv
import re
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=RRIW0YM0PRPMKD9Q'
response = requests.get(url)
print(response)
data = response.json()
print(data)

file_path = Path.cwd()/"mainsolution.py"
file_path2 = Path.cwd()/"mainsolution.py"/"summary_report.txt"




