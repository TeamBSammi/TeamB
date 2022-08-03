#reading cash on hand
from pathlib import Path
import re, csv

file_cohpath = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

def coh_function(forex):
    with file_cohpath.open(mode = "r", encoding = "utf-8") as fileread:
        csvreader = csv.reader(fileread)
        next(csvreader)
        day = []
        coh = []
        for values in csvreader:
            day.append(values[0])
            coh.append(values[1])
    coh1 = 0
    coh2 = -1
    difference = []

    for number in range(0,5):
        coh1 += 1
        coh2 += 1
        difference.append(int(coh[coh1])-(int(coh[coh2])))



#reading profit and loss
from pathlib import Path
import re, csv

file_palpath = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"

def profitloss_function(forex):
    with file_palpath.open(mode = "r", encoding = "utf-8") as filepal:
        csvreaderpal = csv.reader(filepal)
        next(csvreaderpal)
        
        day = []
        profit = []

        
        for values in csvreaderpal:
            day.append(values[0])
            profit.append(values[4])
    pal1 = 0
    pal2 = -1
    diff = []

    for number in range(0,5):
        pal1 += 1
        pal2 += 1
    
    diff.append(int(profit[pal1])-(int(profit[pal2])))

txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

with txtfile.open(mode = "w",newline = "") as file:
    for day,number in enumerate(difference,45):
        writer = csv.writer(file)
        if number < 0:
            writer.writerow(f"[CASH DEFICT] US${abs(number)} on day {day}")
    for day,number in enumerate(diff,45):
        writer = csv.writer(file)
        if number < 0:
            writer.writerow(f"[PROFIT DEFICT] US${abs(number)} on day {day}")



#reading of overheads
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
                maximu = (max(overheads))

print(f"[HIGHEST OVERHEADS] {cat}: {maxover}")

txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

with txtfile.open(mode = "w",newline = "") as file:
    for day,number in enumerate(difference,45):
        writer = csv.writer(file)
        if number < 0:
            writer.writerow(f"[CASH DEFICT] US${abs(number)} on day {day}")
    for day,number in enumerate(diff,45):
        writer = csv.writer(file)
        if number < 0:
            writer.writerow(f"[PROFIT DEFICT] US${abs(number)} on day {day}")
