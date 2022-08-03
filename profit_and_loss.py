from pathlib import Path
import re, csv

file_cohpath = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

def profitandloss_function(forex):
    with file_cohpath.open(mode = "r", encoding = "utf-8") as file1:
        csvreading = csv.reader(file1)
        next(csvreading)
        days = []
        profitandloss = []
        for values in csvreading:
            days.append(values[0])
            profitandloss.append(values[1])
        
    profitandloss1 = 0
    profitandloss2 = -1
    difference = []

    for number in range(0,5):
        profitandloss1 += 1
        profitandloss2 += 1
        difference.append((float(profitandloss[profitandloss1])-(float(profitandloss[profitandloss2]))))

    with txtfile.open(mode = "w",newline = "") as file:
        for day,number in enumerate(difference,45):
            if number < 0:
                file.writelines(f"[PROFTI DEFICT] SGD${(abs(number)*forex)} on day {day}\n")
            elif not number < 0:
                file.writelines(f"[PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")


# file_palpath = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
# fp = Path.cwd()/'summary_report.txt'
# fp.touch()

# def profitloss_function(forex):
#     with file_palpath.open(mode = "r", encoding = "utf-8") as filepal:
#         csvreaderpal = csv.reader(filepal)
#         next(csvreaderpal)

#     day = []
#     profit = []
        
#     for values in csvreaderpal:
#         day.append(values[0])
#         profit.append(values[4])
#     pal1 = 0
#     pal2 = -1
#     diff = []

#     for number in range(0,5):
#         pal1 += 1
#         pal2 += 1
        
#     diff.append(int(profit[pal1])-(int(profit[pal2])))

#     with fp.open(mode = "w",newline = "") as file:
#         for day,number in enumerate(diff,45):
#             if number < 0:
#                 file.writelines(f"[PROFIT DEFICT] US${abs(number)} on day {day}\n")
