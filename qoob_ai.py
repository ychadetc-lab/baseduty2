import serial
import time as tm
import datetime
import os
import sys
import pyttsx3
import random as rd
import requests
import json
import vlc, pafy
import cv2
import pyautogui as pg
import os.path
from pynput.keyboard import Key, Controller
import subprocess


def secure():
    engine = pyttsx3.init()
    engine.say("HELLO, USER, BEFORE YOU USE MEYOU NEED TO LOOK AT MY CAMERA")
    engine.setProperty('rate', 150)
    engine.runAndWait()

    while True:
        file_locate = 'C:\\Users\\Ychad\\Desktop\\'
        i = 'scan'
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        photo = cv2.imwrite(str(i)+'.jpg', image)
        

        del(camera)

        saveLocation = 'C:\\Users\\Ychad\\Desktop\\personal projects\\baseduty\\'
                 

        url = 'https://api-us.faceplusplus.com/facepp/v3/compare'
        params = { 'api_key':'4AZ0mSlXIQxlTPjs0jFSIVNRWW0vgMDS','api_secret':'1iiSymCR6C9qZEmQpRELnFoobSs2xIaA' }
        files = {'image_file1': open(saveLocation+'base.jpg', 'rb'),'image_file2': open(file_locate+'scan.jpg', 'rb')}
        res = requests.post(url,data=params,files=files).text
        json_res = json.loads(res)
        confidence = json_res['confidence']
        if confidence >= 70:
            engine = pyttsx3.init()
            engine.say("Access, Granted!")
            engine.setProperty('rate', 150)
            engine.runAndWait()
            print(confidence)
            qoobee_ai()
            break

        elif confidence < 70:
            

            engine = pyttsx3.init()
            engine.say("Access, Denied!")
            engine.setProperty('rate', 150)
            engine.runAndWait()





def register_base():
    saveLocation = 'C:\\Users\\Ychad\\Desktop\\personal projects\\baseduty\\'
    i = 'base'
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    photo = cv2.imwrite(os.path.join(saveLocation, str(i)+'.jpg') , image)
    del(camera)
    engine = pyttsx3.init()
    engine.say("Face Has been Registered!")
    engine.setProperty('rate', 150)
    engine.runAndWait()
    register()

def register():
    ask = input("registered? y/n?: ")
    if ask == 'y':
       secure()
    elif ask == 'n':
       register_base()
        
def qoobee_facepp():
    i = "scan"
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    photo = cv2.imwrite(str(i)+'.jpg', image)

    del(camera)

    saveLocation = 'C:\\Users\\Ychad\\Desktop\\personal projects\\baseduty\\'
    url = 'https://api-us.faceplusplus.com/facepp/v3/compare'
    params = { 'api_key':'4AZ0mSlXIQxlTPjs0jFSIVNRWW0vgMDS','api_secret':'1iiSymCR6C9qZEmQpRELnFoobSs2xIaA' }
    files = {'image_file1': open(saveLocation+'base.jpg', 'rb'),'image_file2': open(saveLocation+'scan.jpg', 'rb')}
    res = requests.post(url,data=params,files=files).text
    json_res = json.loads(res)
    confidence = json_res['confidence']
    if confidence >= 60:
        engine = pyttsx3.init()
        engine.say("Access, Granted!")
        engine.setProperty('rate', 100)
        engine.runAndWait()

    else:
        

        engine = pyttsx3.init()
        engine.say("Access, Denied!")
        engine.setProperty('rate', 100)
        engine.runAndWait()



def qoobee_ss():
    pyautogui.screenshot('C:\\Users\\Ychad\\Desktop\\personal projects\\baseduty\\screenshots\\image.png')






def qoobee_ai():


                response = {
                      "res1": "hello sir e chad hows your day?",
                      "res2": "what can i do for you?",
                      "res3": "my name is, Qoobee. your AI",
                      "res4": "ok sir e chad!, if you need me just activate me again. Goodbye sir e chad.",
                      "res5": "im sorry sir e chad, i cant respond. would you please try again?",
                      "res6": "please choose operations",
                      "res7": "Enter the firstnumber",
                      "res8": "Enter the secondnumber",
                      "res9": "activating my calculaor",
                      "res10": "activating my built in game",
                      "res11": "Checking my Real Time Clock in my System",
                      "res12": "Checking my weather report system!",
                      "res13": "Opening Qoobee Locator",
                      "res14": "Opening my BMI application",
                      "res15": "Opening Time Alarm System",
                      "res16": "alarm has been set!",
                      "res17": "activating selected executable program",
                      "res18": "opening youtube downloaded videos",
                      "res19": "authorizing qoobee to move mouse in certain directions",
                      "res20": "authorizing qoobee to log in your steam credentials",




                    }
                now = datetime.datetime.now()
                dateStr = now.strftime("%Y-%m-%d")
                month = now.strftime("%m")
                day = now.strftime("%d")
                timeStr = now.strftime("%H:%M:%S")
                time = (f"The current Date and time based on my system is : {dateStr} , {timeStr}")

                def mp3player():
                    song_lib = {
                        "memories" : "https://www.youtube.com/watch?v=SlPhMPnQ58k",
                        "pakinabang" : "https://www.youtube.com/watch?v=Kh53w_hL0Ho",
                        "darkside" : "https://www.youtube.com/watch?v=M-P4QBt-FWw",
                        "ignite" : "https://www.youtube.com/watch?v=qEvS9grK9Bw",
                        "zeb" : "https://www.youtube.com/watch?v=1sVYAyv03S0",
                        "girls like you" : "https://www.youtube.com/watch?v=QCQR7eyaiJM",
                        "earth" : "https://www.youtube.com/watch?v=fBbOgrbpF5E",
                        
                        }


                    y = input("enter song name here: ")

                    x = song_lib.get(y)
                    url = x
                    video = pafy.new(url)
                    best = video.getbest()
                    media = vlc.MediaPlayer(best.url)
                    media.play()


                def do_all():
                    pg.moveTo(654,380, 2)
                    pg.moveTo(1330,360, 2)
                    pg.moveTo(35,383, 2)
                    pg.moveTo(669,5, 2)
                    pg.moveTo(659,757, 2)





                def qoobee_auto():

                 


                    while True:
                        move_mouse = input("Enter where you want to move the cursor: ")
                        if move_mouse == "center":
                           engine = pyttsx3.init()
                           engine.say("moving to center")
                           engine.setProperty('rate', 150)
                           engine.runAndWait()
                           pg.moveTo(654,380, 2)
                        elif move_mouse == "right":
                            engine = pyttsx3.init()
                            engine.say("moving to right")
                            engine.setProperty('rate', 150)
                            engine.runAndWait()
                            pg.moveTo(1330,360, 2)
                        elif move_mouse == "left":
                            engine = pyttsx3.init()
                            engine.say("moving left")
                            engine.setProperty('rate', 150)
                            engine.runAndWait()
                            pg.moveTo(35,383, 2)
                        elif move_mouse == "up":
                            engine = pyttsx3.init()
                            engine.say("moving up")
                            engine.setProperty('rate', 150)
                            engine.runAndWait()
                            pg.moveTo(669,5, 2)
                        elif move_mouse == "down":
                            engine = pyttsx3.init()
                            engine.say("moving down")
                            engine.setProperty('rate', 150)
                            engine.runAndWait()
                            pg.moveTo(659,757, 2)
                        elif move_mouse == "do it all":
                            engine = pyttsx3.init()
                            engine.say("doing it all")
                            engine.setProperty('rate', 150)
                            engine.runAndWait()
                            do_all()
                        elif move_mouse == "close":
                            break





                def run_exe():
                    engine = pyttsx3.init()
                    engine.say("enter a program to be execute")
                    engine.setProperty('rate', 200)
                    engine.runAndWait()

                    exe = input("enter to open an program: ")


                    if exe == "chrome":
                         engine = pyttsx3.init()
                         engine.say("opening google chrome")
                         engine.setProperty('rate', 200)
                         engine.runAndWait()
                         
                         os.system(r'"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
                    else:
                         print("try again")












                def start_alarm():


                    stop = False

                    while stop == False:
                        rn = str(datetime.datetime.now().time())
                        f1 = open("time.txt", "r")
                        x = (f1.read())
                        print(rn)
                       
                    
                        if rn >= x:
                            engine = pyttsx3.init()
                            engine.say("yes its time now!")
                            engine.setProperty('rate', 200)
                            engine.runAndWait()
                           
                            break
                def manual_cursor():
                    time_1 = tm.sleep(6)
                    keyboard = Controller()
                    time_1
                    login = pg.moveTo(705, 317, 2)
                    keyboard.type("ychadetc")
                    time_1
                    passwd = pg.moveTo(640, 355, 2)
                    pg.click()
                    keyboard.type("projectarsenal23")
                    login_click = pg.moveTo(607, 415, 2)
                    pg.click()
                    #cls_ads = pg.moveTo(982, 722, 2)
                    #pg.click()
                    time_1
                    click_HC = pg.moveTo(54, 115, 2)
                    pg.click()
                    time_1
                    click_play = pg.moveTo(336, 206, 2)
                    pg.click()
                    time_1
                    #ychadetc
                    
                def login_steam():
                    
                    subprocess.Popen([r"C:\\Program Files (x86)\\Steam\\Steam.exe"])
                    manual_cursor()
                    

                    
                       
                def setalarm():
                    
                    set_alarm_time = input("Set Time alarm in TT:MM:SS: ")
                    f1 = open("time.txt", "w")
                    f1.write(set_alarm_time)
                    f1.close()
                def alarm_checking():
                    
                    f1 = open("time.txt", "r")
                    x = (f1.read())
                    print(x)
                    print(timeStr)


                def asking():
                    ask_do = input("enter what to do: ")

                    if ask_do == "set alarm":
                        setalarm()
                    elif ask_do == "check":
                        alarm_checking()

                def system_calcu():
                    x = response.get("res6")
                    engine = pyttsx3.init()
                    engine.say(x)
                    engine.setProperty('rate', 150)
                    engine.runAndWait()
                    chooseop = input("type + , x, /, -,: ")
                    x = response.get("res7")
                    engine = pyttsx3.init()
                    engine.say(x)
                    engine.setProperty('rate', 150)
                    engine.runAndWait()
                    num1 = int(input("enter here: "))
                    x = response.get("res8")
                    engine = pyttsx3.init()
                    engine.say(x)
                    engine.setProperty('rate', 150)
                    engine.runAndWait()
                    num2 = int(input("enter here: "))
                    if chooseop == "+":
                        ans = num1 + num2
                        x = ("and the answer in" + str(num1) + "plus" + str(num2) + "is" + str(ans))
                        engine = pyttsx3.init()
                        engine.say(x)
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                        print(ans)
                    elif chooseop == "x":
                        ans = num1 * num2
                        x = ("and the answer in" + str(num1) + "multiplayed by" + str(num2) + "is" + str(ans))
                        engine = pyttsx3.init()
                        engine.say(x)
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                        print(ans)
                    elif chooseop == "/":
                        ans = num1 / num2
                        x = ("and the answer in" + str(num1) + "devided by" + str(num2) + "is" + str(ans))
                        engine = pyttsx3.init()
                        engine.say(x)
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                        print(ans)
                    elif chooseop == "-":
                        ans = num1 - num2
                        x = ("and the answer in" + str(num1) + "minus" + str(num2) + "is" + str(ans))
                        engine = pyttsx3.init()
                        engine.say(x)
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                        print(ans)
                    elif chooseop == "exit":
                        qoobee()
                        
                def game():
                    number = rd.randint(1,100)
                    guesses = 0

                    while guesses < 6:
                        guess = int(input("enter yoour guess here: "))
                        guesses = guesses + 1
                        if guesses == 6:
                             x = "you loose. Betterluck Next Time"
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                        
                             break



                        if guess < 100:
                             x = "your guess is lower than 100"
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                        
                        elif guess > 100:
                             x = "your guess is greater than 100"
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                        

                    if guess == number and guesses != 6:
                         x = "your guess is right! Congratulations!"
                         engine = pyttsx3.init()
                         engine.say(x)
                         engine.setProperty('rate', 150)
                         engine.runAndWait()
                        

                def rtc():

                    now = datetime.datetime.now()
                    dateStr = now.strftime("%Y-%m-%d")
                    timeStr = now.strftime("%H:%M:%S")
                    saying = (f"The current Date and time based on my system is : {dateStr} , {timeStr}")
                    engine = pyttsx3.init()
                    engine.say(saying)
                    engine.setProperty('rate', 150)
                    engine.runAndWait()

                def alarm():
                     engine = pyttsx3.init()
                     engine.say("its christmas day!")
                     engine.setProperty('rate', 150)
                     engine.runAndWait()
                     if month == str(12) and day == str(25):
                         engine = pyttsx3.init()
                         engine.say("its christmas day!")
                         engine.setProperty('rate', 150)
                         engine.runAndWait()

                def led():
                    ser = serial.Serial(
                    port ='COM6', 
                    baudrate = 9600,
                    parity = serial.PARITY_ODD, 
                    stopbits = serial.STOPBITS_TWO, 
                    bytesize = serial.EIGHTBITS

                    )
                def weather():
                    
                    engine = pyttsx3.init()
                    engine.say("enter the city here")
                    engine.setProperty('rate', 150)
                    engine.runAndWait()

                    city = input("enter city: ")
                    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=03d1230a2d5262de4b971c1924176b70'.format(city)
                    res = requests.get(url)
                    data = res.json()
                    engine = pyttsx3.init()
                    engine.say(data)
                    engine.setProperty('rate', 150)
                    engine.runAndWait()
                    qoobee()

                 

                    while 1:                                      
                        input_data = str(input())                  
                        print ("you entered", input_data)           
                    
                        if (input_data == str('1')):                    
                            ser.write(str.encode('1'))      
                            engine = pyttsx3.init()
                            engine.say("L E D is on!")
                            engine.setProperty('rate', 150)
                            engine.runAndWait()
                       
                    
                        if (input_data == str('0')):                   
                            ser.write(str.encode('0'))             
                            engine = pyttsx3.init()
                            engine.say("L E D is off!")
                            engine.setProperty('rate', 150)
                            engine.runAndWait()
                        elif input_data == "exit":
                            break
                def iplocator():
                    
                    engine = pyttsx3.init()
                    engine.say("Enter the Ip here")
                    engine.setProperty('rate', 150)
                    engine.runAndWait()
                    ip = input("enter ip: ")
                    url = 'http://ip-api.com/json/'
                    res = requests.get(url + ip)
                    data = res.json()
                    query1=("here is the ip of the target sir: " , data['query'])
                    city1=("and here is the city based on qoobee sigthing: " , data['city'])
                    lat_lon=("latitude", data['lat'], "longitude", data['lon'])
                    country=("and this is the country: ", data['country'])


                    engine = pyttsx3.init()
                    engine.say(query1)
                    engine.setProperty('rate', 150)
                    engine.runAndWait()
                    print(data['query'])

                    engine = pyttsx3.init()
                    engine.say(city1)
                    engine.setProperty('rate', 150)
                    engine.runAndWait()
                    print(data['city'])

                    engine = pyttsx3.init()
                    engine.say(lat_lon)
                    engine.setProperty('rate', 150)
                    engine.runAndWait()
                    print(data['lat'] , data['lon'])

                    engine = pyttsx3.init()
                    engine.say(country)
                    engine.setProperty('rate', 150)
                    engine.runAndWait()
                    print(data['country'])








                def greet():
                    if timeStr < str(12):
                            

                        engine = pyttsx3.init()
                        engine.say("goodmorning, sir e chad")
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                    elif timeStr >= str(12) and timeStr < str(17):
                        engine = pyttsx3.init()
                        engine.say("good afternoon, sir e chad")
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                    elif timeStr > str(17) and timeStr < str(23):
                        engine = pyttsx3.init()
                        engine.say("good evening, sir e chad")
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                    else:
                        engine = pyttsx3.init()
                        engine.say("hi, sir e chad")
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                def BMI():
                    w = float(input("Enter weight here: "))
                    h = float(input("enter height here: "))
                    height = h ** 2
                    result = w/height

                    if result < 25.00 and result >= 18.00:
                        engine = pyttsx3.init()
                        engine.say("you are normal")
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                       
                    elif result > 25.00 and result <= 30.00:
                        engine = pyttsx3.init()
                        engine.say("you are overweight")
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                        
                    elif result > 30.00 and result <= 40.00:
                        engine = pyttsx3.init()
                        engine.say("Obesity")
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                        
                    elif result > 40.00:
                        engine = pyttsx3.init()
                        engine.say("morbid obesity")
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                        
                    else:
                        engine = pyttsx3.init()
                        engine.say("invalid input")
                        engine.setProperty('rate', 150)
                        engine.runAndWait()
                        

                            
                    

                        


                def qoobee():
                    x = response.get("res3")
                    engine = pyttsx3.init()
                    engine.say(x)
                    engine.setProperty('rate', 150)
                    engine.runAndWait()
                    while True:
                   
                        rep = input("reply: ")
                        if rep == "shutdown":
                             x = response.get("res4")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                        
                             exit()
                        elif rep == "whats up":
                             x = response.get("res2")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                        elif rep == "whats your name again?":
                             x = response.get("res3")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                        elif rep == "hello qoobee" or rep == "hi qoobee":
                             x = response.get("res1")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                        elif rep == "calculator":
                             x = response.get("res9")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             system_calcu()
                        elif rep == "lets play a game":
                             x = response.get("res10")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             game()
                        elif rep == "qoobee current time":
                             x = response.get("res11")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             rtc()
                        elif rep == "greet me":
                         
                             greet()
                        elif rep == "arduino":
                             engine = pyttsx3.init()
                             engine.say("opening arduino port serial")
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             led()
                        elif rep == "report weather":
                             x = response.get("res12")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             weather()
                        elif rep == "qoobee locator":
                             x = response.get("res13")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             iplocator()
                        elif rep == "qoobee BMI":
                             x = response.get("res14")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             BMI()
                        elif rep == "alarm time":
                             x = response.get("res15")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             asking()
                        elif rep == "time set":
                             x = response.get("res16")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             start_alarm()
                        elif rep == "open exe":
                             x = response.get("res17")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             run_exe()
                        elif rep == "entertain":
                             x = response.get("res18")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             mp3player()
                        elif rep == "move mouse":
                             x = response.get("res19")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             qoobee_auto()
                        elif rep == "qoobee login steam":
                             x = response.get("res20")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             login_steam()
                        elif rep == "qoobee login":
                             x = response.get("res20")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                             manual_cursor()
                            
                        
                            
                            
                                    
                                    

                         
                        else:
                             x = response.get("res5")
                             engine = pyttsx3.init()
                             engine.say(x)
                             engine.setProperty('rate', 150)
                             engine.runAndWait()
                        

                greet()       
                qoobee()

register()        
                   

    
    
