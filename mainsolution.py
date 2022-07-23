import requests
from pathlib import Path
import re, csv

file_path = Path.cwd()/"TeamB"
#file_csv = Path.cwd()/"TeamB"/"tenancy.csv"
#file_csv.touch()

url = "https://github.com/TeamBSammi/TeamB.git"
response = requests.get(url)
print(response)

data = response.json()
print(data)

