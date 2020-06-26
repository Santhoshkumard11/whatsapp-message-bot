from pyautogui import *
from time import sleep
import sys
import webbrowser as wb

#contact list
contacts = ["$name","$name"]
message = "Hello"

#idle for 7 seconds
sleep(7)

# method to find the search bar location
def click_search_name(name):
    x1, y1 = [211,250]

    moveTo(x1, y1)
    click()
    typewrite(name, interval=0.2)
    sleep(2)
    press('enter')

# method to find and send message
def click_send_message(msg):
    x3, y3 = [950,750]
    moveTo(x3, y3)
    click()
    sleep(2)
    typewrite(msg)
    press('enter')

#iterating through the contact list
for index,name in contacts:
    try:
        click_search_name(name)
    except:
        print("Unable to locate search bar or name")

    try:
        click_send_message(message)
    except:
        print("Unable to locate message bar")


print('Messages sent successfully')
