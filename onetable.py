
import os
from time import gmtime, strftime, localtime
import time
import datetime
from colorama import Fore, Back, Style

from datetime import datetime
#time_one = time.time()

#clear screen
os.system('clear')

#initialize variables
player_name = str()
now_time = time.time()
now_time_read = strftime("%a, %d %b %Y %H:%M:%S", localtime())
table_number = "ONE"
table_open = "AVAILABLE"
table_closed = "IN PLAY"

table_status = table_open
start_time = ()
start_read = " "
stop_time = ()
stop_read = ""
total_time = ()

hourly_rate = 10
minute_rate = 10/60
second_rate = 10/60/60

def main():

    global table_status
    global start_read
    global start_time
    print("\n")
    if table_status == table_open:
        print(f" Table {table_number} is AVAILABLE")
    elif table_status == table_closed:
        print(f" Table {table_number} is {Fore.RED}{table_status}{Style.RESET_ALL} since {start_read}")
    print("\n")
    print("SELECT AN OPTION FROM BELOW")
    print(" 1 - Start Session")
    print(" 2 - End Session")
    print("\n")
    print("Enter 'Q' to quit")
    option = input("--->  ")
    if option == "1" and table_status == table_closed:
        os.system('clear')
        print("xxxxxxxxxxxxxxxxxx")
        print("Pick another table")
        print("xxxxxxxxxxxxxxxxxx")
        main()
    elif option == "1":
        os.system('clear')
        table_status = table_closed
        start_time = time.time()
        start_read = strftime("%a, %d %b %Y %H:%M:%S", localtime())
        main()    
    elif option == "2" and table_status != table_closed:
        os.system('clear')
        print("Table is not in use.  Pick an active table")
        main()
    elif option == "2":
        os.system('clear')
        stop_time = time.time()
        total_time =(stop_time - start_time)/60
        money_due = total_time * minute_rate
        dollars = f"{money_due:.2f}"
        print(f"Your Session lasted {total_time} minutes")
        print(f"You owe me ${dollars}")
        main()
    elif option.casefold() == "q":
        pass
    else:
        
        os.system('clear')
        print("Try again")
        main()


        


main()
#print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
#print(time.time())

