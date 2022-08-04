from pathlib import Path
import re, csv
from sre_constants import CATEGORY
from unicodedata import category
from api import forex

#reading of overheads
file_opath = Path.cwd()/"csv_reports"/"overheads-day-40.csv"
txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

def overheads_function():
    with file_opath.open(mode = "r", encoding = "utf-8") as fileread:
        csvreadero= csv.reader(fileread)
        next(csvreadero)
        category = []
        overheads = []
        for values in csvreadero:
            category.append(values[0])
            overheads.append(values[1])
        with txtfile.open(mode = "a",newline = "") as file:    
            for i, amount in enumerate(values):
                if amount == max(values):
                    file.writeline(f"[HIGHEST OVERHEADS] {category[overheads]}: SGD{float(amount)*forex}" )