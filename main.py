import api
import read_file
import write_file

def main():
    forex = api.api_function()
    read_file.read_file_function(forex)
    write_file.write_file_function(forex)

main()