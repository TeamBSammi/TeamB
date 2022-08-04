from pathlib import Path
import re, csv


file_opath = Path.cwd()/"csv_reports"/"overheads-day-40.csv"

def overheads_function(forex):
    with file_opath.open(mode = "r", encoding = "utf-8") as fileread:
        csvreadero= csv.reader(fileread)
        next(csvreadero)
        
        category = []
        overheads = []
        amount = []
        for amount in csvreadero:
            category.append(amount[0])
            overheads.append(amount[1])
            cat= max(amount)
            # maxoverheads= max(overheads)
            for maxover in amount:
                maximum = (max(overheads))
                print (f"[HIGHEST OVERHEADS] {cat}: {maxover}")
    print(overheads_function(forex))
# print (f"[HIGHEST OVERHEADS] {cat}: {maxover}")