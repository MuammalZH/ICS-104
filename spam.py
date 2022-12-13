import pyautogui
import time 
numOfTimes = 0


spamLetter =input("Enter What do you want to spam: ")
timesToSpam = int(input("How many Times do you want to spam the word? "))
time.sleep(5)

while timesToSpam > numOfTimes:
    pyautogui.press(spamLetter)
    # time.sleep(0.3) # how fast do u want it to print
    pyautogui.press("enter")
    numOfTimes +=1
print("Done.")