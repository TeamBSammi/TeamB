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
        profit.append(values[1])
pal1 = 0
pal2 = -1
diff = []

for number in range(0,5):
    pal1 += 1
    pal2 += 1
    
    diff.append(int(profit[pal1])-(int(profit[pal2])))

print(diff)
for day,amount in enumerate(diff,45):
    
    if number < 0:
        print(f"[PROFIT DEFICT] DAY {day}, AMOUNT : SGD{abs(number)}")
    else:
        print(f"[PROFIT] DAY {day}, AMOUNT : SGD{abs(number)}")





   # profit45=re.findall(pattern=r"45.+",string=read)
  #  day45=[0][0:1].rstrip()
  #  print(day45)