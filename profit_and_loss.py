#Import path to start out the code which provides an object for working with files and directories.
from pathlib import Path
# import re is to set specifies set of stringd that matches it and import csv is to create a object from items in csv
import re, csv

from api import forex

file_cohpath = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

def profit_and_loss_function(forex):
    with file_cohpath.open(mode = "r", encoding = "utf-8") as file1:
        csvreading = csv.reader(file1)
        next(csvreading)
        days = []
        profitandloss = []
        for values in csvreading:
            days.append(values[0])
            profitandloss.append(values[4])
        
    profitandloss1 = 0
    profitandloss2 = -1
    difference = []

    for number in range(0,5):
        profitandloss1 += 1
        profitandloss2 += 1
        difference.append((float(profitandloss[profitandloss1])-(float(profitandloss[profitandloss2]))))

    with txtfile.open(mode = "a",newline = "",encoding="utf-8") as file:
        for day,number in enumerate(difference,45):
            if number < 0:
                file.write(f"[PROFIT DEFICT]  DAY: {day}, AMOUNT: {(abs(number)*forex)}\n")
            else:
                if min(difference) > 0:
                    file.write(f"[PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")

profit_and_loss_function(forex)

