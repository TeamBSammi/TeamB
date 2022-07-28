from dataclasses import dataclass
from pathlib import Path
import re, csv

file_cohpath = Path.cwd()/"TeamB"/"csv_reports"/"cash-on-hand-usd.csv"

for file in file_cohpath.glob("*.txt"):
    with file.open(mode = "r", encoding = "utf-8",) as fileread:

        csvreader = csv.reader(fileread)
        
print(csvreader)