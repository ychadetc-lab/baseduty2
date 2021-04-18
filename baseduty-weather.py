#!/usr/local/bin/python
import serial
import time as t
from datetime import datetime
import pyttsx3
ser = serial.Serial('/dev/ttyACM0', 9600)
def weather_():
    n = 0

    while True:
         
        t.sleep(1)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        n = n + 1
        
        #print("Current Time =", current_time)
        s = ser.readline()
        x = (s.decode("utf-8"))
  
        print("BASEDUTY WEATHER STATION")
        print(x)
        print(current_time)
        upt = x+" "+current_time
       
        if n == 5:
            f=open("wupdate.txt", "w")
            f.write(x)
            f.close
            n = n - 5
            
            pass
            

weather_()

