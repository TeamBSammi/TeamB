from pathlib import Path
import re, csv

file_palpath = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"


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

print(diff)

txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

with txtfile.open(mode = "w",newline = "") as file:
    for day,number in enumerate(diff,45):
        writer = csv.writer(file)
        if number < 0:
            writer.writerow(f"[PROFIT DEFICT] US${abs(number)} on day {day}")


