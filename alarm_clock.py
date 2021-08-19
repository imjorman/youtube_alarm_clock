# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:11:30 2021

@author: Jordan Kennedy (Twitter: @imjorman)
"""

import sys

inputs = [userInput for userInput in sys.argv]

if len(inputs) != 4:
    print("Use format: <hour> <minute> <am/pm>.  You gave too many inputs.")
    
if inputs[1].isnumeric() == False or inputs[2].isnumeric() == False:
    print("Use format: <hour> <minute> <am/pm>.  Hour and minute should be whole numbers.")

if inputs[3].lower() == 'am' or inputs[3].lower() == 'pm':
    print("All things worked here")
else:
    print("Use format: <hour> <minute> <am/pm>.  Make sure you put am or pm.")