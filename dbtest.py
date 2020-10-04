from tkinter import *
from tkinter import ttk
from pymysql import *
from tkinter import messagebox
import mysql.connector

import pymysql
user = 'school'
passw = 'apnaquetta'


windows = Tk()
windows.geometry('800x500')
windows.title('login screen')
fram = Frame(windows,bd=4,relief=RIDGE,bg='blue')
fram.place(width=500,height=200,x=150,y=100)

user_var= StringVar()
pass_var= StringVar()

roll = Label(fram,text='username',bg='blue',fg='white',font=('times new roman',20,'bold'))
roll.grid(row=0,column=0,pady=10,padx=20,sticky='w')

user=Entry(fram,textvariable=user_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
user.grid(row=0,column=1,pady=10,padx=20,sticky='w')


ro = Label(fram,text='password',bg='blue',fg='white',font=('times new roman',20,'bold'))
ro.grid(row=1,column=0,pady=10,padx=20,sticky='w')

passw=Entry(fram,textvariable=pass_var,show="*",font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
passw.grid(row=1,column=1,pady=10,padx=20,sticky='w')

def login_user():
    if user_var.get()=="school" and pass_var.get()=="apnaquetta":
        windows.destroy()
        import fee
        print('Success')
    else:
        message = Label(fram,text="invalid username or pasword")
        message.grid(row=3,column=1,columnspan=10)


addbtn = Button(fram,text='login',width=10,command=login_user).grid(row=2,column=0,columnspan=10,padx=10,pady=10)

windows.mainloop()
