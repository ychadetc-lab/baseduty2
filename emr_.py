import mysql.connector
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "mydatabase",
    port = 3307
    
    )
print(mydb)
mycursor = mydb.cursor()

def showinf_w():
    global y
    global results
    top4 = tk.Tk()
    top4.title("EMR INFORMATIONS")
    top4.geometry("400x400")
        
    print("welcome to your information")
    #show_info = input("type you want to show info: ")
    
    sql = ("SELECT * FROM informations WHERE uname = %s")
    val = (user_name)
    mycursor.execute(sql, (val,))

    results = mycursor.fetchall()
    
    for y in results:
        print(y[0])
        print(y[1])
        print(y[2])
        print(y[3])
        print(y[4])
        print(y[5])



    healthstats_ = (y[0])
    weights_ = (y[1])
    meds_ = (y[2])
    ages_ = (y[3])
    nams_ = (y[4])
    unames_ = (y[5])
    lb6 = tk.Label(top4, text = "WELCOME TO YOUR INFORMATION USER:"+" "+unames_, font = fontStyle).pack()
    lb4 = tk.Label(top4, text = "Name:"+" "+nams_).pack()
    lb3 = tk.Label(top4, text = "Age:"+" "+ages_+" "+"y/o").pack()
    lb2 = tk.Label(top4, text = "Weight:"+" "+weights_).pack()
    lb1 = tk.Label(top4, text = "Health Status:"+" "+healthstats_).pack()
    lb5 = tk.Label(top4, text = "Medicine:"+" "+meds_).pack()
    tk.mainloop()
    
    
    
    #lb5 = tk.Label(top4, text = "Health Status:"+" "+healthstats_).pack()
    #lb1 = tk.Label(top4, text = "Health Status:"+" "+healthstats_).pack()
    
    
    

def signup_w():
    global top3
    global fname_
    global address_
    top3 = tk.Tk()
    top3.title("EMR Sign Up")
    top3.geometry("400x400")
    fname_ = tk.StringVar()
    address_ = tk.StringVar()
    lbl6 = tk.Label(top3, text = "Full Name").pack()
    t3 = tk.Entry(top3,textvariable=fname_).pack()
    lbl7 = tk.Label(top3, text = "Address").pack()
    t4 = tk.Entry(top3,textvariable=address_).pack()
    b8 = tk.Button(top3, text = "complete", width = 20, command = fullname_ ).pack()
    tk.mainloop()
    

def fillup_w():
    global top2
    global heltstats_
    global weight_
    global medicines_
    global age_
    global name_
    global uname_
    
    top2 = tk.Tk()
    top2.title("EMR fillup")
    top2.geometry("400x400")
    
    heltstats_ = tk.StringVar()
    weight_ = tk.StringVar()
    medicines_ = tk.StringVar()
    age_ = tk.StringVar()
    name_ = tk.StringVar()
    uname_ = tk.StringVar()
    lbl50 = tk.Label(top2, text = "Health Status").pack()
    t45 = tk.Entry(top2,textvariable=heltstats_).pack()
    lbl10 = tk.Label(top2, text = "Weight").pack()
    t46 = tk.Entry(top2,textvariable=weight_).pack()
    lbl11 = tk.Label(top2, text = "Medicines").pack()
    t47 = tk.Entry(top2,textvariable=medicines_).pack()
    lbl12 = tk.Label(top2, text = "Age").pack()
    t48 = tk.Entry(top2,textvariable=age_).pack()
    lbl13 = tk.Label(top2, text = "Name").pack()
    t49 = tk.Entry(top2,textvariable=name_).pack()
    lb14 = tk.Label(top2, text = "Username").pack()
    t50= tk.Entry(top2,textvariable=uname_).pack()
    b90 = tk.Button(top2, text = "Complete", width = 20, command = more_fillup).pack()
    tk.mainloop()




def more_fillup():
    top2.destroy()
    global helt_stats
    global _weight
    global _medicines
    global _age
    global _name
    global _uname

    helt_stats = heltstats_.get()
    _weight = weight_.get()
    _medicines = medicines_.get()
    _age = age_.get()
    _name  = name_.get()
    _uname = input_name 
    
    sql = "INSERT INTO informations(health_status, weight, medicines, age, name, uname) VALUES(%s, %s, %s, %s, %s, %s)"
    #print("please fill up more informations")
    

    
    
    val = (helt_stats, _weight, _medicines, _age, _name, _uname)
    mycursor.execute(sql, val)
    mydb.commit()
    print("info has been added! thankyou for choosing tkemr")


def exist_user():
    top.destroy()
    global user_name
    #top.destroy()
    user_name = user_.get()
    pass_word = passwd_.get()

    sql = ("SELECT * FROM users WHERE name = %s")
    val = (user_name)
    mycursor.execute(sql,(val,))
    
    results = mycursor.fetchall()
    for x in results:
        #print(x)
        #print(type(x))
        if x[1] == pass_word and x[0] == user_name:
            #print("hello"+' '+ x[3])
            #print("you are from"+" "+x[4])
            #show_inf()
            showinf_w()
            
            
        else:
            print("user doesn't exist")
            break

def register():
    top.destroy()
    global input_name
    global input_pass
    input_name = user_.get()
    input_pass = passwd_.get()

    sql = ("SELECT COUNT(1) FROM users WHERE name = %s")
    val = (input_name)
    
    mycursor.execute(sql,(val,))
    results = mycursor.fetchall()
    print(results)
    x1 = results[0][0]
    if x1 > 0:
        print("user exist!")
        return None

    else:
        global fname
        signup_w()

def fullname_():
        top3.destroy()
        global fname
        


        
        sql = "INSERT INTO users(name, password) VALUES (%s, %s)"
        val = (input_name, input_pass)
        mycursor.execute(sql, val)
        mydb.commit()
        print(input_name +" "+"and"+" "+input_pass +" "+"has been registered!")

        fname = fname_.get()
        sql = "UPDATE users SET fullname = (%s) WHERE name = (%s)"
        val = (fname, input_name)
        mycursor.execute(sql, val)
        mydb.commit()
        print("fullname hasbeen added!")

        addr = address_.get()
        sql = "UPDATE users SET address = (%s) WHERE name = (%s)"
        val = (addr, input_name)
        mycursor.execute(sql, val)
        mydb.commit()
        print("address hasbeen added")
        
        fillup_w()
def delete_acc():
    dame = input("put account name to delete: ")
    #sql = "UPDATE users SET name = %s WHERE name = (%s)"
    sql = "DELETE FROM users WHERE name = %s"
    val = (dame)
    
    mycursor.execute(sql, (val,))
    mydb.commit()
    print("account of"+" "+ dame +" "+"has been deleted!")


def add_fname():
    global fname
    fname = input("enter your full name: ")
    sql = "UPDATE users SET fullname = %s WHERE name = 'input_name'"
    val = (fname)
    mycursor.execute(sql,(val,))
    mydb.commit()
    print("fullname hasbeen added!")


def show_inf():
    global y
    global results
    print("welcome to your information")
    #show_info = input("type you want to show info: ")
    
    sql = ("SELECT * FROM informations WHERE uname = %s")
    val = (user_name)
    mycursor.execute(sql, (val,))

    results = mycursor.fetchall()
    
    for y in results:
        print(y[0])
        print(y[1])

global fontStyle
top = tk.Tk()
top.title("EMR")
top.geometry("400x400")
user_ = tk.StringVar()
passwd_ = tk.StringVar()
fontStyle = tkFont.Font(family="Lucida Grande", size = 20)
lbl = tk.Label(top, text = "Electronic Medical Records", font=fontStyle).pack()
lbl1 = tk.Label(top, text = "Username").pack()
t = tk.Entry(top,textvariable=user_).pack()
lbl2 = tk.Label(top, text = "Password").pack()
t2 = tk.Entry(top, show = "*",textvariable=passwd_).pack()
b = tk.Button(top, text = "Log in", width = 20, command = exist_user).pack()
b2 = tk.Button(top, text = "Sign Up", width = 20, command = register ).pack()
tk.mainloop()



