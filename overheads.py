from pathlib import Path
import re, csv
from api import forex

#reading of overheads
file_opath = Path.cwd()/"csv_reports"/"overheads-day-40.csv"
txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

def overheads_function(forex):
    with file_opath.open(mode = "r", encoding = "utf-8") as fileread:
        csvreadero= csv.reader(fileread)
        next(csvreadero)
        
        category= []
        overheads =[]
        for values in csvreadero:
            category.append((values[0]))
            overheads.append((values[1])) 
            # dict_ov = category, overheads
            # print(dict_ov)
            # print(category)
            # over = max(overheads)
            # cat = max(category)
            # mini= min (category)
            # print(category[over])
        print (values)
            #maxcat= re.findall(pattern=(over)* , string = csv)
            # with txtfile.open(mode = "a",newline = "") as file:
            #     for num in overheads: 
            #         file.writelines(f"[HIGHEST OVERHEADS] {cat}: SGD ${over*forex})\n")
            #         break
#         print (max(category))
#         print(min(category))
#         print(f"[HIGHEST OVERHEADS] {mini}: SGD ${over}")
# overheads_function(forex)            
    # with txtfile.open(mode = "w",newline = "") as fileo:
    #         for num in overheads:
    #             fileo.writelines(f"[HIGHEST OVERHEADS] {cat}: {maximum}")
                # with txtfile.open(mode = "a",newline = "") as file:
                #     for num in overheads: 
                #         file.writelines(f"[HIGHEST OVERHEADS] {cat}: US${(abs(maximum)*forex)}")
                #         break

overheads_function(forex)
