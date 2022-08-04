from pathlib import Path
import re, csv
from api import forex

#iterates over the overheads csv file 
file_opath = Path.cwd()/"csv_reports"/"overheads-day-40.csv"
#create a new file path and extend it to the current working directory and create a new file "summary_report.txt"
txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

#creating a function with the parameter of forex
def overheads_function(forex):
    #with statement is used to make the code more readable and cleaner
    #reading of the overheads csv file
    with file_opath.open(mode="r",encoding = "UTF-8") as fileread:
        csvreadero=csv.reader(fileread)
        next(csvreadero)

        #create two empty list category and overheads for the two different part of the list
        category = []
        overheads = []

        #for loops is used to repeat the block of codes
        for values in csvreadero:
            #append the data into empty list 
            category.append(values[0])
            overheads.append(values[1]) 

    #using for loop in a range of the length of values to convert into float
    for x in range(0, len(overheads)):
        overheads[x] = float(overheads[x])

    #writing of the data extracted into the txt file 
    with txtfile.open(mode = "a",newline = " ") as file:
        #for loops is used to repeat the block of codes
        #enumerate() method adds a counter to the iterable and returns it 
        for expense,values in enumerate(overheads):
            #== will show if both the values are true or equate to one another it will write the statement into the new txt file created
            #max is used to extract the highest value in the 'overheads' list
            if values == max(overheads):
                #writing of code,use of .upper() to uppercase all the letters, multiplying forex data from api to overheads amount to convert to SGD from USD
                file.writelines(f"[HIGHEST OVERHEADS] {(category[expense]).upper()}: SGD ${float(values)*forex}\n")

overheads_function(forex)