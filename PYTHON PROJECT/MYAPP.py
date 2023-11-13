from tkinter import *
import tkinter as t
import mysql.connector
import datetime as d
from tkinter import messagebox

db=mysql.connector.connect(
    host='localhost',
    user='Anish',
    password='anish',
    database='myapp')

cs=db.cursor()

cls12=''

columnname=''

total=0

def take():
    global columnname
    if cls12=='class12a':
        time=d.datetime.today()
        columnname=str(time.day)+'_'+str(time.month)+'_'+str(time.year)
        a='alter table class12a add '+columnname+" char(20) DEFAULT 'ABSENT'"
        cs.execute(a)
        
    else:
        time=d.datetime.today()
        columnname=str(time.day)+'_'+str(time.month)+'_'+str(time.year)
        a='alter table class_12_b add '+columnname+' char(20)'
        cs.execute(a)
        
def percentage():
    global columnname
    global total
    if cls12=='class12a':
        cs.execute('select count(*) from class12a')
        for i in cs:
            total=int(i[0])
        a='select count(*) from class12a where '+columnname+"='PRESENT' group by "+columnname
        cs.execute(a)
        for i in cs:
            present=int(i[0])
        percentage=(present/total)*100
        messagebox.showinfo('PRESENT PERCENTAGE',str(present)+' PRESENT OUT OF '+str(total)+"\nPRESENT PERCENTAGE="+str(percentage)+'%')
            
def present():
    cs.execute("USE myapp")
    roll=e1.get()
    disp='ROLL NO. '+roll+' IS MARKED PRESENT'
    messagebox.showinfo('INFO!',disp)
    print('ROLL NO. '+roll+' of '+cls12+ ' is PRESENT')
    if cls12=='class12a':
        b="UPDATE class12a set "+columnname+"='PRESENT' where roll="+roll
        cs.execute(b)
        db.commit()
    else:
        b="UPDATE class_12_b set "+columnname+"='PRESENT' where roll="+roll
        cs.execute(b)
        db.commit()
        
def clsa():
    global cls12
    cls12='class12a'
    
def clsb():
    global cls12
    cls12='S_b'
    
w=t.Tk()

w.geometry('500x350')

w.title("MYAPP")

t.Label(w,
        text='STUDENT ATTENDANCE',
        font='ELEPHANT 18',
        height=2,
        bg='black',
        fg='white'
        ).grid(row=0,column=1)

t.Label(w,
        text='SELECT CLASS'
        ).grid(row=1,column=0)

r1=Radiobutton(w,
               text='CLASS 12 A',
               value=1,
               command=clsa
               ).grid(row=1,column=1)

r2=Radiobutton(w,
               text='CLASS 12 B',
               value=2,
               command=clsb
               ).grid(row=2,column=1)

t.Label(w,
        text="ENTER YOUR ROLL NO."
        ).grid(row=4,column=0)

t.Label(w,
        text="TO BE MARKED PRESENT"
        ).grid(row=5,column=0)

e1=t.Entry(w)

e1.grid(row=4,column=1)

b1=t.Button(w,
            text='Enter',
            width='10',
            command=present,
            fg='green',
            bg='black'
            ).grid(row=6,column=0)

b2=t.Button(w,
            text='Exit',
            width='10',
            command=w.destroy,
            fg='red',
            bg='black'
            ).grid(row=7,column=0)

b3=t.Button(w,
            text='TAKE ATTENDANCE',
            width='15',height='3',
            command=take,
            fg='blue',
            bg='black'
            ).grid(row=3,column=1)

b4=t.Button(w,
            text='ATTENDANCE PERCENTAGE OF THE DAY',
            width='35',height='3',
            command=percentage,
            fg='yellow',
            bg='black'
            ).grid(row=8,column=1)

w.mainloop()
