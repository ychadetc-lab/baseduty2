import cv2
import datetime
import time as t
from subprocess import call
import subprocess
print("updater running...")
def send_pics():
    print("updating site....")
    now = datetime.datetime.now().strftime("%I:%M:%S %p" )

    path = '/var/www/html/aajax/'
    i = 'hope'
    camera = cv2.VideoCapture('http://192.168.43.201:8080/video')
    return_value, image = camera.read()

    photo = cv2.imwrite("hope.jpg", image)
    print(photo)
    cv2.waitKey(0)
    t.sleep(5)
    del(camera)
    '''
    img = cv2.imread('hope.jpg', 1)
    cv2.imwrite(os.path.join(path , 'hope.jpg'), img)
    cv2.waitKey(0)
    '''
    subprocess.call("mv"+" "+"/home/pi/hope.jpg"+" "+"/var/www/html/aajax", shell=True)
     
while True:
    now = datetime.datetime.now().strftime("%I:%M:%S %p" )
    now2 = datetime.datetime.now().strftime("%M:%S" )
    #print(now2)
    lst_min = ["05:00", "10:00", "15:00", "20:00", "25:00", "30:00", "35:00", "40:00", "45:00", "50:00", "55:00", "00:00"]
    if now2 in lst_min:
        send_pics()
        pass
    
