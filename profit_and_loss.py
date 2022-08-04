#Import path to start out the code which provides an object for working with files and directories.
from pathlib import Path
# import re is to set specifies set of stringd that matches it and import csv is to create a object from items in csv
import re, csv
#import currency
from api import forex

# file path to find the file
file_cohpath = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
txtfile = Path.cwd()/"summary_report.txt"
# to create a file
txtfile.touch()

# to create a function
def profit_and_loss_function(forex):
    #use this function to read the file
    with file_cohpath.open(mode = "r", encoding = "utf-8") as file1:
        csvreading = csv.reader(file1)
        next(csvreading)
        # create list of days
        days = []
        # create list for profit and loss
        profitandloss = []
        # use this function to add value in csvreading
        for values in csvreading:
            # use .append and choose value 0 as days is the file number 
            days.append(values[0])
            #use.append and choose value 4 as profit and loss is the 4th number in the profit and loss csv file
            profitandloss.append(values[4])

     # use profitandloss1 to create variable to caculate the amount in days list 
    profitandloss1 = 0
    # use profitandloss1 to create variable to caculate the amount in profitandloss list 
    profitandloss2 = -1
    # create a list for difference
    difference = []

# to make sure all the values is inside
    for number in range(0,5):
        # create profitandloss1 to add amount in
        profitandloss1 += 1
        #create profitandloss2 to add amount in
        profitandloss2 += 1
        #use function .append and caculate the value to know if it is defict or surplus
        difference.append((float(profitandloss[profitandloss1])-(float(profitandloss[profitandloss2]))))
#use this function to write down the days and amount 
    with txtfile.open(mode = "a",newline = "",encoding="utf-8") as file:
        for day,number in enumerate(difference,45):
            # use if function and when the number is less than 0 what will happen
            if number < 0:
                # write  the day and amount
                file.write(f"[PROFIT DEFICT]  DAY: {day}, AMOUNT: {round((abs(number)*forex),2)}\n")
                # use else function 
            else:
                # if the amount is more than 0 
                if min(difference) > 0:
                    #show if amount is more than o
                    file.write(f"[PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
                    break

profit_and_loss_function(forex)

