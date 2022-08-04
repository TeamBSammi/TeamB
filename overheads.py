from pathlib import Path
import re, csv


#reading of overheads
file_opath = Path.cwd()/"csv_reports"/"overheads-day-40.csv"
txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

def overheads_function(forex):
    with file_opath.open(mode = "r", encoding = "utf-8") as fileread:
        csvreadero= csv.reader(fileread)
        next(csvreadero)
        
        category = []
        overheads = []
        for values in csvreadero:
            category.append([0])
            overheads.append([1])
            cat= max(values)
            amount=[]
            for num in amount:
                amount.append(overheads_function(forex))
                maximum = (max(overheads))
                cat= max(values)
                
    with txtfile.open(mode = "w",newline = "") as fileo:
            for num in overheads:
                fileo.writelines(f"[HIGHEST OVERHEADS] {cat}: {maximum}")
                
        
        
        # #for loop is used to iterate the elements
        # for tenant in combine:
        #     # .append() it is used to add a single item to the list 
        #     empty.append(tenant)
        #     # Use .writerow() to write single line and iterate over a for loop.
        #     writer.writerow(tenant)
