


#table_numbers = []

import os
from time import gmtime, strftime, localtime
import time
import datetime
import colorama
from colorama import Fore, Style, Back
from datetime import datetime
#time_one = time.time()

#clear screen
os.system('clear')

#initialize variables
player_name = str()
now_time = time.time()
now_time_read = strftime("%a, %d %b %Y %H:%M:%S", localtime())
table_numbers = ["ONE", "TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","ELEVEN","TWELVE"]
object_tables = []
#table_status = [table_open,table_open,table_open,table_open,table_open,table_open,table_open,table_open,table_open,table_open,table_open,table_open]
table_open = "AVAILABLE"
table_closed = "IN PLAY"

table_status = table_closed
start_time = ()
start_read = " "
stop_time = ()
stop_read = ""
total_time = ()
total_time_read = ""
table_number = ""

hourly_rate = 10
minute_rate = 10/60
minute_rate = 10/60/60

class Table:
   


    def __init__(self, table_number):
        self.table_status = table_status
        self.start_read = start_read
        self.start_stime = start_time
        self.table_number = table_number

    def __repr__(self):
        return (f" {self.table_number}")
        #return (f"{self.table_numbers}")#return (f"{self.table_status}|{self.start_read}| {self.start_time}")   
        
    

    
    
    
       
    
        

    
def main():
    pass
    #global table_status
    #global start_read
    #global start_time
    #table_numbers[0].table_status = table_closed
    
    
            

        
def create_tables():
    for each in table_numbers:
        object_table = Table(each)  
        object_tables.append(object_table)
        
create_tables()

print(object_tables)
        
        
        
def select_action():
    option = input("--->  ")
    if option == "1":
        check_out()
    elif option == "2":
        check_in()    
    
   

    
    # make function to open table already open
def not_closed():    
    os.system('clear')
    print("xxxxxxxxxxxxxxxxxx")
    print("Pick another table")
    print("xxxxxxxxxxxxxxxxxx")
    main()

#make function to start using available table
def check_out():
    os.system('clear')
    display()
    selection = input("Select a table:  ")
    if selection.isdigit() == True and selection < 0 and selection < 13 and selection.table_status == table_closed:
        
        os.system('clear')
        print("xxxxxxxxxxxxxxxxxx")
        print("Pick another table")
        print("xxxxxxxxxxxxxxxxxx")
        display()
        check_out()


    table_status = table_closed
    start_time = time.time()
    start_read = strftime("%a, %d %b %Y %H:%M:%S", localtime())
    main()    

# make function if closing an unused table
def not_open():
    if option == "2" and table_status != table_open:
        os.system('clear')
        print("Table is not in use.  Pick an active table")
        main()

# make function to close table
def check_in(): 
    if option == "2":
        os.system('clear')
        table_status = table_open
        stop_time = time.time()
        total_time =(stop_time - start_time)/60
        money_due = total_time * minute_rate
        dollars = f"{money_due:.2f}"
        print(f"Your Session lasted {total_time:.2f} minutes")
        print(f"You owe me ${dollars}")
        main()


# make function to press q to quit
def quit():   
    if option.casefold() == "q":
        pass
    
    else:          
        os.system('clear')
        print("Try again")
        main() 

def display():
    print("\n")
    i = 1
    for each1 in object_tables:
        if table_status == table_open:
            print(f"{i} - Table {each1} is {table_open}")
        elif table_status == table_closed:
            print(f"{i} - Table {each1} is {table_closed} since {start_read}")
        i = i + 1
    print("\n")

    
    
    
def firstchoice():
    print("\n")
    print("SELECT AN OPTION FROM BELOW")
    print(" 1 - Start Session")
    print(" 2 - End Session")
    print("\n")
    print("Enter 'Q' to quit")
    #option = input("--->  ")
    select_action()
    
#def select_table():
    #selection = input("Select a table:  ")
    #if selection.isdigit() == True and selection < 0 and selection < 13:
            
       

 

    
    

       
def startscreen():
    display()
    firstchoice() 
startscreen()

 