import datetime
import time as t
import vlc
import pyttsx3
import pyautogui as pg
import pymsgbox

        
    
def alarm():
    while True:
        now = datetime.datetime.now().strftime("%I:%M:%S %p" )
        now1 = datetime.datetime.now().strftime("%I:%M:%S %p %B %d, %Y" )
        now2 = datetime.datetime.now().strftime("%I:%M %p" )
            
        print(now2.lower())
        t.sleep(1)
        
        f=open("/var/www/html/aajax/wupdate1.txt", "w")
        f.write(now1)
        f.close
      
        lst = ["01:00:00 PM", "02:00:00 PM", "03:00:00 PM", "04:00:00 PM", "05:00:00 PM", "06:00:00 PM"]
        lst1 = ["01:00:00 AM", "02:00:00 AM", "03:00:00 AM", "04:00:00 AM", "05:00:00 AM", "06:00:00 AM", "07:00:00 AM", "08:00:00 AM", "09:00:00 AM", "10:00:00 AM", "11:00:00 AM"]
        lst2= ["07:00:00 PM", "08:00:00 PM", "09:00:00 PM", "10:00:00 PM", "11:00:00 PM"]
        if now in lst:
            engine = pyttsx3.init()
            engine.setProperty('volume', 10)
            engine.setProperty('rate', 150)
            engine.say("GOOD AFTER NOON SIR ECHAD, THE TIME NOW IS")
            engine.runAndWait()
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.say(now)
           
            
            engine.runAndWait()
            pymsgbox.alert(text='Sir Ychad!'+" "+"it's already"+" "+now, title='FYI SIR', button='OK', timeout=20000 )
            
            
            
            
            pass
            
            
             
        elif now in lst1:
            engine = pyttsx3.init()
            engine.setProperty('volume', 10)
            engine.setProperty('rate', 150)
            engine.say("GOOD MORNING SIR ECHAD, THE TIME NOW IS")
            engine.runAndWait()
            engine = pyttsx3.init()
            engine.say(now)
            engine.setProperty('rate', 150)
            
            engine.runAndWait()
            
            pymsgbox.alert(text='Sir Ychad!'+" "+"it's already"+" "+now, title='FYI SIR', button='OK', timeout=20000)
            
            pass
           
            

        elif now in lst2:
            engine = pyttsx3.init()
            engine.setProperty('volume', 10)
            engine.setProperty('rate', 150)
            engine.say("GOOD EVENING SIR ECHAD, THE TIME NOW IS")
            engine.runAndWait()
            engine = pyttsx3.init()
            engine.say(now)
            engine.setProperty('rate', 150)
            
            engine.runAndWait()
            pymsgbox.alert(text='Sir Ychad!'+" "+"it's already"+" "+now, title='FYI SIR', button='OK', timeout=20000  )
            
            pass
            
            

        elif now == "12:00:00 AM":
            engine.setProperty('volume', 10)
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.say("SIR ECHAD IT'S ALREADY")
            engine.runAndWait()
            engine = pyttsx3.init()
            engine.say(now)
            engine.setProperty('rate', 150)
            
            engine.runAndWait()
            pymsgbox.alert(text='Sir Ychad!'+" "+"it's already"+" "+now, title='FYI SIR', button='OK', timeout=20000  )
            pass
            
            
            

        elif now =="12:00:00 PM":
            
            engine = pyttsx3.init()
            engine.setProperty('volume', 10)
            engine.setProperty('rate', 150)
            engine.say("HAVE A GOOD NOON SIR ECHAD")
            engine.runAndWait()
            engine = pyttsx3.init()
            engine.say(now)
            engine.setProperty('rate', 150)
            
            engine.runAndWait()
            pymsgbox.alert(text='Sir Ychad!'+" "+"it's already"+" "+now, title='FYI SIR', button='OK', timeout=20000  )
            pass
   
alarm()


