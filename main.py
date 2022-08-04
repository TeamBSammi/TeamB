import api, cash_on_hand#, overheads, profit_and_loss
from pathlib import Path

fp = Path.cwd()/'summary_report.txt'
fp.touch()

def main():
    forex = api.api_function()
    #overheads.overheads_function(forex)
    cash_on_hand.cash_on_hand_function()
    #profit_and_loss.profit_loss_function(forex)
    
print(main())