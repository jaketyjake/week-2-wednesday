#pool table management program

#import databases

import os
from time import gmtime, strftime, localtime
import time

from datetime import datetime

#clear screen
os.system('clear')

#initialize variables
player_name = str()
table_occupied = False
now_time = strftime("%a, %d %b %Y %H:%M:%S", localtime())
start_time = strftime("none")
stop_time = strftime("none")

table_numbers = {"ONE" : (), "TWO"  : (), "THREE" : (), "FOUR" : (), "FIVE" : (), "SIX" : (), "SEVEN" : (), "EIGHT" : (), "NINE" : (), "TEN" : (), "ELEVEN" : (), "TWELVE" : ()}

#table_numbers_dict = {
#    "ONE" : (player_name, ),
#    "TWO" : (),
#    "THREE" : (),
#    "FOUR" : (),
#    "FIVE" : (),
#    "SIX" : (),
#    "SEVEN" : (),
#    "EIGHT" : (),
#    "NINE" : (),
#    "TEN" : (),
#    "ELEVEN" : (),
#    "TWELVE" : (),
#    }


    



class Table:
    def __init__(self,table_number, table_occupied):
        self.table_number = table_number
        self.table_occupied = False


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        
class StartTime:
    def __init__(self, start_time):
        self.start_time = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    #def current_time(self):
    #now_time = strftime("%a, %d %b %Y %H:%M:%S", gmtime())    
        
class EndTime:
    def __init__(self, end_time):
        self.end_time = end_time


for each in table_numbers:
    print(f"Table {each}")







#below time looks like --> Wed, 09 May 2018 16:58:21
# it also can not be used in algorithms due it being NAIVE
print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))
print(now_time)

# don't use below method :looks like --> 11:58:21.952720
print(datetime.now().time())

