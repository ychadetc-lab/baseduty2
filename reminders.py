from tkinter import *
from tkcalendar import Calendar
import sqlite3
import datetime
now = datetime.datetime.now().strftime("%I:%M:%S %p" )
# Create Object
root = Tk()
  
# Set geometry
root.geometry("500x400")
root.title("Event Scheduler")
  
# Add Calender
cal = Calendar(root, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
  
cal.grid(column = 1)
 #set the date 
def grad_date():
    global c
    #time monitoring
    now = datetime.datetime.now().strftime("%I:%M:%S %p" )
    #time declaration
    declared_time = datetime.datetime.now().strftime("%I:%M %p" )
    #logic key time in seconds
    time_condition = datetime.datetime.now().strftime("%S" )

    date.config(text = "Selected Date is: " + cal.get_date())
    conn = sqlite3.connect('ES.db')
    c = conn.cursor()
    '''
    c.execute("""CREATE TABLE personnels(
           event_name text,
           from_time text,
           to_time text,
           name text
   


            )""")
    conn.commit()
    conn.close()
    '''
    '''
    c.execute("ALTER TABLE personnels ADD COLUMN declared_date text")
    conn.commit()
    conn.close()
    '''
    
    #insert data
    #values_ = (str(en_up3_).lower(), str(from_up1_).lower(), str(to_up2_).lower(), str(enter_name_up4_).lower(), str(cal.get_date()).lower())
    #sql = ('INSERT INTO personnels (event_name, from_time, to_time, name, declared_date) VALUES (?, ?, ?, ?, ?)', values_) 
    c.execute('INSERT INTO personnels VALUES (?, ?, ?, ?, ?)', (eventName, fromHour, toHour, enterName, calendarSelect))
    conn.commit()
    #conn.close()
    
    c.execute("SELECT * FROM personnels")
    rows = c.fetchall()
    for row in rows:
        print(row)
  
# Add Button and Label
Button(root, text = "Set Date",
       command = grad_date).grid(row = 8, column = 1)

from_up1 = StringVar()

to_up2 = StringVar()

en_up3 = StringVar()

enter_name_up4 = StringVar()

#to sring

from_up1_ = from_up1.get()

to_up2_ = to_up2.get()

en_up3_ = en_up3.get()

enter_name_up4_ = enter_name_up4.get()

#insert final data
eventName = en_up3_

fromHour = from_up1_

toHour = to_up2_

enterName = enter_name_up4_

calendarSelect = cal.get_date()

#date confirmation  
date = Label(root, text = "")
date.grid(row = 9,column = 1)
#forms
lbl3 =  Label(root, text = 'Event Name:').grid(row = 4, column = 0)
e3 = Entry(root,bd = 5, textvariable = en_up3 ).grid(row = 4, column = 1)

lbl1 =  Label(root, text = 'FROM:').grid(row = 5, column = 0)
e = Entry(root,bd = 5, textvariable = from_up1 ).grid(row = 5, column = 1)

lbl2 =  Label(root, text = 'TO:').grid(row = 6, column = 0)
e1 = Entry(root,bd = 5, textvariable = to_up2 ).grid(row = 6, column = 1)

lbl4 =  Label(root, text = 'Enter your Name:').grid(row = 7, column = 0)
e4 = Entry(root,bd = 5, textvariable = enter_name_up4 ).grid(row = 7, column = 1)
  
# Excecute Tkinter
root.mainloop()
'''
conn = sqlite3.connect('ES.db')
c = conn.cursor()
c.execute("SELECT * FROM personnels")
rows = c.fetchall()
for row in rows:
    print(row)
'''
  
