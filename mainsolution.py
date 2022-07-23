import requests
from pathlib import Path
import re, csv

url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATEfrom_symbol=USDto_symbol=SGD"
response = requests.get(url)
print(response)
data = response.json()
print(data)

file_path = Path.cwd()/"mainsolution.py"
file_path2 = Path.cwd()/"mainsolution.py"/"currencyexchangerate.txt"
file_path2.touch()
print(file_path2.exists())



