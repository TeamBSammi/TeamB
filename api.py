import requests
from pathlib import Path
import re, csv

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=RRIW0YM0PRPMKD9Q'
response = requests.get(url)
data = response.json()
print(data)

#file_path = Path.cwd()/"TeamB"
#file_path2 = Path.cwd()/"TeamB"/"summary_report.txt"
#file_path2.touch()
#print(file_path2.exists())

#file_path2.touch()


#if file_path2.exists():
#    with file_path2.open('w', encoding = 'UTF-8', newline = '') as file:
#        writer = csv.writer(file)
#        test = "test = "
#        for item in data.values():
#             writer.writerow([item["5. Exchange Rate"]])
#        
#    file.close()

#else:
#    print("file path does not exists")



txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

with txtfile.open(mode = "w",newline = "") as file:
    for day,number in enumerate(difference,45):
        writer = csv.writer(file)
        if number < 0:
            writer.writerow(f"[CASH DEFICT] US${abs(number)} on day {day}")