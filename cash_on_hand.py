from pathlib import Path
import re, csv
from api import forex

file_cohpath = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

#defining a function called cash_on_hand_function
def cash_on_hand_function(forex):
    #reading the file in the cash on hand csv
    with file_cohpath.open(mode = "r", encoding = "utf-8") as fileread:
        csvreader = csv.reader(fileread)
        next(csvreader)
        #created 2 empty list for day and the values for cash on hand
        day = []
        coh = []
        #using appending as a re-defined method used to add values to csvreader
        for values in csvreader:
            #as day is first, it is 0 while coh is 1
            day.append(values[0])
            coh.append(values[1])
    #creating a code to get values for 2 different days in order to calculate the difference
    coh1 = 0
    coh2 = -1
    #in order to calculate the difference of the list of values, created another list for difference
    difference = []
    #using for loop in a range of 6 values as required
    for number in range(0,5):
        #in order to add on the numbers, += 1 was used
        coh1 += 1
        coh2 += 1
        #to calculate the difference of the values for cash on hand
        difference.append((float(coh[coh1])-(float(coh[coh2]))))
    #to write the cash on hand in the summary report txt file
    with txtfile.open(mode = "a",newline = "") as file:
        for day,number in enumerate(difference,45):
            #as a deficit dumber contains "-", creating a if function to define whether in all the datas there are any deficit
            if number < 0:
                file.writelines(f"[CASH DEFICT] DAY: {day}, AMOUNT: {(abs(number)*forex)}\n")
            #as deficit is 
            else:
                #using if function to check if the lowest number in difference is more than 0 in order to prevent it from spawning with cash deficit
                if min(difference) > 0:
                    file.writelines(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

cash_on_hand_function(forex)
