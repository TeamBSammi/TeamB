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
for number in range(0,5):
    coh1 += 1
    coh2 += 1
    #the formula to calculate the difference of the cash on hand integers
    difference.append(int(coh[coh1])-(int(coh[coh2])))

#for day,number in enumerate(difference,45):
#    #this formula is for when the number captured is negative after the difference is caluclated to be used
#    if number < 0:
#        #to print the data and turn the negative cash on hand number to positive
#        print(f"[CASH DEFICT] US${abs(number)} on day {day}")
#    else:
#        #to print the data and turn the negative cash on hand number to positive
#        print(f"[CASH SURPLUS] Cash-on-hand on each period is higher than the previous period ")

file_csv = Path.cwd()/"summary_report.txt"
file_csv.touch()

with file_csv.open(mode = "w",newline = "") as file:
    for day,number in enumerate(difference,45):
        writer = csv.writer(file)
    #this formula is for when the number captured is negative after the difference is caluclated to be used
        if number < 0:
            #to print the data and turn the negative cash on hand number to positive
            writer.writerow(f"[CASH DEFICT] US${abs(number)} on day {day}")
        #else:
        #    writer.writerow(f"[CASH SURPLUS] Cash-on-hand on each period is higher than the previous period ")

    #header = ["ADDRESS", "FLAT", "START DATE", "END DATE", "RENTAL"]
    #writer = csv.writer(file)
    #writer.writerow (header)

