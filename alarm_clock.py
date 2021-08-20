import sys, random, webbrowser
from time import localtime, strftime

inputs = [userInput for userInput in sys.argv] #storing command line arguments into a list
    
#Check to make sure user input correct items
if len(inputs) != 4: #checking to make sure only 3 additional arguments given
    print("Use format: <hour>[space]<minute> <am/pm>.  You gave too many inputs.")
    exit()
    
if inputs[1].isnumeric() == False or inputs[2].isnumeric() == False: #making first two provided inputs are numbers
    print("Use format: <hour>[space]<minute> <am/pm>.  Hour and minute should be whole numbers.")
    exit()
    
if int(inputs[1]) > 12 or int(inputs[1]) < 1 or int(inputs[2]) > 59 or int(inputs[2]) < 1:
    print("Your hours are greater than 12 or less than 1.  Or you have too many minutes.  Please use a 12 hour clock.")
    exit()
    
if inputs[3].lower() == 'am' or inputs[3].lower() == 'pm': #making sure last input is either am or pm
    print() #Why doesn't the inverse work for this, check sometime
else:
    print("Use format: <hour>[space]<minute> <am/pm>.  Make sure you put am or pm.")
    exit()
    

ourTime = strftime("%I:%M %p", localtime()) #grabbs local computer time as 12 hr clock

#This block converts hours and minutes less than 10 to have a zero to match strftime method
input_hour = inputs[1]
if int(input_hour) < 10:
    if input_hour[0] != "0":
        input_hour = "0" + input_hour
input_minute = inputs[2]
if int(input_minute) < 10:
    if input_minute[0] != "0":
        input_minute = "0" + input_minute
input_am_pm = inputs[3].upper() #puts PM or AM as upper since that's what the time module does
inputTime = f"{input_hour}:{input_minute} {input_am_pm}"
    
print("The current time is: " + ourTime)
print("The alarm is set for " + inputTime)

#check the time until the two times match, when they do, flip the inputTime variable
while True:
    ourTime = strftime("%I:%M %p", localtime()) #grabbs local computer time as 12 hr clock
    if inputTime == ourTime:
        break

#Now that we've broken from the loop, we'll do the thing we want when the timer goes off
with open("video_list.txt") as f: #reads each line of text file into a list
    lines = f.readlines()

random = random.randint(0, len(lines)-1) #generates random number to pick a video

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")) #registers chrome as the browser of choice
webbrowser.get('chrome').open(lines[random]) #uses the random number to open a random url from the list in the browser
