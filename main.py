# importing each files as modules to coordinate & execute functions
import api
import read_file
import write_file

# creating all functions for each modules in the main file
def main():
    forex = api.api_function()
    overheads.overheads_function(forex)
    cash_on_hand.coh_function(forex)
    profit_and_loss.profitloss_function(forex)

# execute
main()