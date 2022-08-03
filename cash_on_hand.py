from pathlib import Path
import re, csv

file_cohpath = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

def cashonhand_function(forex):
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
        difference.append((float(coh[coh1])-(float(coh[coh2]))))

    with txtfile.open(mode = "w",newline = "") as file:
        for day,number in enumerate(difference,45):
            if number < 0:
                file.writelines(f"[CASH DEFICT] US${(abs(number)*forex)} on day {day}\n")
            elif not number < 0:
                file.writelines(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
