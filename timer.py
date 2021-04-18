import datetime
import time as t
import pyttsx3
import pyautogui as pg
import pymsgbox
now = datetime.datetime.now().strftime("%I:%M:%S %p")
#time strip
now2 = datetime.datetime.now().strftime("%M")
#enter the value
entermsg = input("enter timeout call: ")
enter_minute = int(input("enter minute: "))
sec_conv = enter_minute * 60
#set the new time
engine = pyttsx3.init()
engine.setProperty('volume', 10)
engine.setProperty('rate', 150)
engine.say("the timer has been set to" + str(enter_minute) +"minutes")
engine.runAndWait()
x = 0
#loop through the time
while True:
    t.sleep(1)
    x = x + 1
    sec = datetime.datetime.now().strftime("%S")
    print(sec)
    #print(newTime)
    if x == sec_conv:
        engine = pyttsx3.init()
        engine.setProperty('volume', 10)
        engine.setProperty('rate', 150)
        engine.say("The time is over, Sir Echad" )
        engine.runAndWait()
        pymsgbox.alert(text=entermsg, title='FYI SIR', button='OK', timeout=20000 )
        
        x = x - sec_conv
        break

 
    
    
