from pathlib import Path
import re, csv
from read_file import difference, diff

txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

with txtfile.open(mode = "w",newline = "") as file:
    for day,number in enumerate(difference,45):
        if number < 0:
            file.writelines(f"[CASH DEFICT] US${abs(number)} on day {day}\n")
    for day,number in enumerate(diff,45):
        if number < 0:
            file.writelines(f"[PROFIT DEFICT] US${abs(number)} on day {day}\n")
