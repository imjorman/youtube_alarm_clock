# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:11:30 2021

@author: Jordan Kennedy (Twitter: @imjorman)
"""

import sys, sys
from time import localtime, strftime

inputs = [userInput for userInput in sys.argv] #storing command line arguments into a list
    
#Check to make sure user input correct items
if len(inputs) != 4: #checking to make sure only 3 additional arguments given
    print("Use format: <hour> <minute> <am/pm>.  You gave too many inputs.")
    exit()
    
if inputs[1].isnumeric() == False or inputs[2].isnumeric() == False: #making first two provided inputs are numbers
    print("Use format: <hour> <minute> <am/pm>.  Hour and minute should be whole numbers.")
    exit()
    
if int(inputs[1]) > 12 or int(inputs[1]) < 1 or int(inputs[2]) > 59 or int(inputs[2]) < 1:
    print("Your hours are greater than 12 or less than 1.  Or you have too many minutes.  Please use a 12 hour clock.")
    exit()
    
if inputs[3].lower() == 'am' or inputs[3].lower() == 'pm': #making sure last input is either am or pm
    print() #Why doesn't the inverse work for this, check sometime
else:
    print("Use format: <hour> <minute> <am/pm>.  Make sure you put am or pm.")
    exit()
    

ourTime = strftime("%I:%M %p", localtime()) #grabbs local computer time as 12 hr clock

#This block converts hours and minutes less than 10 to have a zero to match strftime method
input_hour = inputs[1]
if int(input_hour) < 10:
    input_hour = "0" + input_hour
input_minute = inputs[2]
if int(input_minute) < 10:
    input_minute = "0" + input_minute
input_am_pm = inputs[3].upper() #puts PM or AM as upper since that's what the time module does
inputTime = f"{input_hour}:{input_minute} PM"
    
print("The current time is: " + ourTime)
print("The alarm is set for " + inputTime)

#check the time until the two times match, when they do, flip the inputTime variable
while True:
    ourTime = strftime("%I:%M %p", localtime()) #grabbs local computer time as 12 hr clock
    if inputTime == ourTime:
        break

#Now that we've broken from the loop, we'll do the thing we want when the timer goes off
print("The time has arrived!")
