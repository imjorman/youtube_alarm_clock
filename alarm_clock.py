# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:11:30 2021

@author: Jordan Kennedy (Twitter: @imjorman)
"""

import sys
from time import localtime, strftime

ourTime = strftime("%I:%M %p", localtime()) #grabbing local computer time

inputs = [userInput for userInput in sys.argv] #storing command line arguments into a list

if len(inputs) != 4: #checking to make sure only 3 additional arguments given
    print("Use format: <hour> <minute> <am/pm>.  You gave too many inputs.")
    
if inputs[1].isnumeric() == False or inputs[2].isnumeric() == False: #making first two provided inputs are numbers
    print("Use format: <hour> <minute> <am/pm>.  Hour and minute should be whole numbers.")
    
if int(inputs[1]) > 12 or int(inputs[1]) < 1 or int(inputs[2]) > 12 or int(inputs[2]) < 1:
    print("Your hours are greater than 12 or less than 1.  Please use a 12 hour clock.")

if inputs[3].lower() == 'am' or inputs[3].lower() == 'pm': #making sure last input is either am or pm
    print("All things worked here")
else:
    print("Use format: <hour> <minute> <am/pm>.  Make sure you put am or pm.")

input_hour = int(inputs[1]) #converting the user inputs into variables
input_minute = int(inputs[2])
input_am_pm = inputs[3].upper() #puts PM or AM as upper since that's what the time module does
    
print("The current time is: " + ourTime)