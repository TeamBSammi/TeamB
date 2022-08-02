#reading cash on hand file
from pathlib import Path
import re, csv

file_cohpath = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

#to read the file
with file_cohpath.open(mode = "r", encoding = "utf-8") as fileread:
    csvreader = csv.reader(fileread)
    next(csvreader)
    #creating list with no elements
    day = []
    coh = []

    #as day in the CSV is the first value before the cash on hand it will be 0 value while amount will be 1
    for values in csvreader:
        day.append(values[0])
        coh.append(values[1])
coh1 = 0
coh2 = -1
difference = []
#looping the values. as there are 6 values in total, the range is 0 to 5
for numbers in range(0,5):
    coh1 += 1
    coh2 += 1
    #the formula to calculate the difference of the cash on hand integers
    difference.append(int(coh[coh1])-(int(coh[coh2])))
print(difference)
for day,number in enumerate(difference,45):
    #this formula is for when the number captured is negative after the difference is caluclated to be used
    if number < 0:
        #to print the data and turn the negative cash on hand number to positive
        print(f"[CASH DEFICT] DAY {day}, AMOUNT : SGD{abs(number)}")

# reading of overheads


file_opath = Path.cwd()/"csv_reports"/"overheads-day-40.csv"
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


