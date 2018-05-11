


table_numbers = ["ONE", "TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","ELEVEN","TWELVE"]

import os
from time import gmtime, strftime, localtime
import time
import datetime

from datetime import datetime
#time_one = time.time()

#clear screen
os.system('clear')

#initialize variables
player_name = str()
now_time = time.time()
now_time_read = strftime("%a, %d %b %Y %H:%M:%S", localtime())
table_numbers = ["ONE", "TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","ELEVEN","TWELVE"]
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
minute_rate = 10/60/60

class Table:
   
    def __init__(self, table_status, start_read, start_time):
        self.table_status = table_status
        
        self.start_read = start_read
        self.start_stime = start_time
        
    
    
    def main(self):
        self.stable_status = table_open
        global table_status
        global start_read
        global start_time
        print("\n")
        i = 1
        for each in table_numbers:
            if self.table_status == table_open:
                print(f"{i} - Table {each} is {table_open}")
            elif self.table_status == table_closed:
                print(f"{i} Table {each} is {table_closed} since {self.start_read}")
            i = i + 1
        print("\n")
        
        selection = input("Select a table:  ")
        if selection.isdigit() == True and  selection < 0 and selection < 13:
            self.select_table(selection)

        
       
        elif selection != int:
            os.system('clear')
            print("Please enter the 'number' of the table")
            self.main()
            

       
        
        
        
        
        
        
    def select_table(self, selection):
        
        
        print("\n")
        print("SELECT AN OPTION FROM BELOW")
        print(" 1 - Start Session")
        print(" 2 - End Session")
        print("\n")
        print("Enter 'Q' to quit")
        option = input("--->  ")
        if option == "1" and self.table_status == table_closed:
            os.system('clear')
            print("xxxxxxxxxxxxxxxxxx")
            print("Pick another table")
            print("xxxxxxxxxxxxxxxxxx")
            self.main()
        elif option == "1":
            os.system('clear')
            table_status = table_closed
            self.start_time = time.time()
            self.start_read = strftime("%a, %d %b %Y %H:%M:%S", localtime())
            self.main()    
        elif option == "2" and table_status != table_closed:
            os.system('clear')
            print("Table is not in use.  Pick an active table")
            self.main()
        elif option == "2":
            os.system('clear')
            table_status = table_open
            stop_time = time.time()
            total_time =(stop_time - start_time)/60
            money_due = total_time * minute_rate
            dollars = f"{money_due:.2f}"
            print(f"Your Session lasted {total_time:.2f} minutes")
            print(f"You owe me ${dollars}")
            self.main()
        elif option.casefold() == "q":
            pass
        else:          
            os.system('clear')
            print("Try again")
            self.main()
        

table_one = Table(table_open, start_read, start_time)
table_two = Table(table_open, start_read, start_time)
table_three = Table(table_open, start_read, start_time)
table_four = Table(table_open, start_read, start_time)
table_five = Table(table_open, start_read, start_time)
table_six = Table(table_open, start_read, start_time)
table_seven = Table(table_open, start_read, start_time)
table_eight = Table(table_open, start_read, start_time)
table_nine = Table(table_open, start_read, start_time)
table_ten = Table(table_open, start_read, start_time)
table_eleven = Table(table_open, start_read, start_time)
table_twelve = Table(table_open, start_read, start_time)

table_one.main()
       


