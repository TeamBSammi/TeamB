import api
import read_file
import write_file

def main():
    forex = api.api_function()
    overheads.overheads_function(forex)
    cash_on_hand.coh_function(forex)
    profit_and_loss.profitloss_function(forex)

main()