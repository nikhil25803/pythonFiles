# import imp
import os



print(os.listdir(path='./standard_library'))

from datetime import date

today = date.today()
print("Today's day is: ", today.day)
print("Today's month is: ", today.month)
print("Today's day is: ",today.year)