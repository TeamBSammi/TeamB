from pathlib import Path
import re, csv
from read_file import difference, diff

txtfile = Path.cwd()/"summary_report.txt"
txtfile.touch()

with txtfile.open(mode = "w",newline = "") as file:
    for day,number in enumerate(difference,45):
        writer = csv.writer(file)
        if number < 0:
            writer.writerow(f"[CASH DEFICT] US${abs(number)} on day {day}")
    for day,number in enumerate(diff,45):
        writer = csv.writer(file)
        if number < 0:
            writer.writerow(f"[PROFIT DEFICT] US${abs(number)} on day {day}")
