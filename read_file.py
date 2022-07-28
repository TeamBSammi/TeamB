from dataclasses import dataclass
from pathlib import Path
import re, csv

file_cohpath = Path.cwd()/"TeamB"/"csv_reports"/"cash-on-hand-usd.csv"

with file_cohpath.open(mode = "r", encoding = "utf-8",) as fileread:
    csvreader = csv.reader(fileread)
    next(csvreader)
print(csvreader)