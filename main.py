# import each python file as modules
import api, cash_on_hand, overheads, profit_and_loss
# import path function from pathlib
from pathlib import Path

# writing a function named main() to use all imported modules
def main():
    # setting filepath
    fp = Path.cwd()/'summary_report.txt'
    fp.touch()
    # functions in each modules
    # forex - real time exchange rate
    # retrieve forex with .forex from api
    forex = api.forex
    # opening a file using 'with' and 'open' keyword in 'write' mode
    # and one more parameter 'newline' to remove extra line ending in csv file
    with fp.open(mode = "w",newline = "") as file:
        # functions in each module
        api.api_function()
        overheads.overheads_function(forex)
        cash_on_hand.cash_on_hand_function(forex)
        profit_and_loss.profit_and_loss_function(forex)

# execute function to execute imported functions from all four py files
(main())