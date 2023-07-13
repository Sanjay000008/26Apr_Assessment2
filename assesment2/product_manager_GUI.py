import tkinter
from tkinter import ttk,messagebox
import pymysql

dbcon=pymysql.connect(host='localhost',user='root',password='',database='product_management')
cur=dbcon.cursor()
try:
    cur.execute('use product_management')
except:
    cur.execute('create database product_management')
    cur.execute('use product_management')
try:
    cur.execute('describe ragistration')
except:
    cur.execute('create table ragistration(id int auto_increment primary key,name varchar(30) notnull,contact int(10) unique,email varchar(35) unique,gender text,city text,state text')

window=tkinter.Tk()
window.title("Registration Form")
window.geometry("500x700")
window.config(background='grey')
r=tkinter.StringVar()
r.set('Male')
d=tkinter.StringVar()
m=tkinter.StringVar()

l1=tkinter.Label(text='    Name*',bg='grey',font='Fixedays 15',fg='black').place(x=0,y=30)
l2=tkinter.Label(text='    Contact*',bg='grey',font='Fixedays 15',fg='black').place(x=0,y=80)
l3=tkinter.Label(text='    Email*',bg='grey',font='Fixedays 15',fg='black').place(x=0,y=130)
l4=tkinter.Label(text='    Gender*',bg='grey',font='Fixedays 15',fg='black').place(x=0,y=180)
l5=tkinter.Label(text='    City*',bg='grey',font='Fixedays 15',fg='black').place(x=0,y=230)
l6=tkinter.Label(text='    State*',bg='grey',font='Fixedays 15',fg='black').place(x=0,y=280)

e1=tkinter.Entry(font='Fixedays 15',fg='black')
e1.place(x=120,y=30)
e2=tkinter.Entry(font='Fixedays 15',fg='black')
e2.place(x=120,y=80)
e3=tkinter.Entry(font='Fixedays 15',fg='black')
e3.place(x=120,y=130)
e4=tkinter.Radiobutton(value='Male',text='Male',variable=r,bg='grey',font='Fixedays 15',fg='black').place(x=120,y=180)
e4=tkinter.Radiobutton(value='female',text='female',variable=r,bg='grey',font='Fixedays 15',fg='black').place(x=220,y=180)
e5=ttk.Combobox(textvariable=d)
e5['values']=('Rajkot','Jamnagar','Pune','Ahemdabad','Banglor','Delhi','Dwarka','Kolkata','ranchi','ujain','bhopal')
e5.place(x=120,y=230)
e5.current()

e6=ttk.Combobox(textvariable=m)
e6['values']=('Gujrat','Maharastra','Karnataka','Delhi','WestBengol','Zarkhand','Madhyapradesh')
e6.place(x=120,y=280)
e6.current()
def btnclick():
    s=f"insert into ragistration(name,contact,email,gender,city,state) values('{e1.get()}','{e2.get()}','{e3.get()}','{(r.get())}','{e5.get()}','{e6.get()}')"
    try:
        cur.execute(s)
        dbcon.commit()
        print("Record Inserted Sussefully")
    except Exception as e:
        print(e)
    else:
        e1.delete('0','end')
        e2.delete('0','end')
        e3.delete('0','end')
        e5.delete('0','end')
        e6.delete('0','end')


b=tkinter.Button(text="Register",bg='gold',font='Fixedays 15',fg='black',command=btnclick).place(x=230,y=350)

tkinter.mainloop()