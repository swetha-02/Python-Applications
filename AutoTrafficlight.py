from tkinter import *
from time import sleep
count=25
def start():
    counter(count)

def red():
    canvas1. create_oval(110,110,20,20,outline='white', fill='red',width='3')
    canvas2.create_oval(110, 110, 20, 20, outline='white', fill='white', width='3')
    canvas3.create_oval(110, 110, 20, 20, outline='white', fill='white', width='3')

def orange():
    canvas1.create_oval(110, 110, 20, 20, outline='white', fill='white', width='3')
    canvas2.create_oval(110, 110, 20, 20, outline='white', fill='orange', width='3')
    canvas3.create_oval(110, 110, 20, 20, outline='white', fill='white', width='3')

def green():
    canvas1.create_oval(110, 110, 20, 20, outline='white', fill='white', width='3')
    canvas2.create_oval(110, 110, 20, 20, outline='white', fill='white', width='3')
    canvas3.create_oval(110, 110, 20, 20, outline='white', fill='green', width='3')

def intervals(c):
    if c>15:
        red()
        timeinterval.config(text=c)
        play.update()
        sleep(1)
        counter(c)
    elif c>10 and c<=15:
        orange()
        timeinterval.config(text=c)
        play.update()
        sleep(1)
        counter(c)
    elif c>0 and c<=10:
        green()
        timeinterval.config(text=c)
        play.update()
        sleep(1)
        counter(c)
    elif c==0:
        red()
        timeinterval.config(text=c)
        play.update()
        sleep(1)
        counter(c)

def counter(data):
    if data>0:
        data=data-1
        intervals(data)

play=Tk()
play.geometry('300x450')
play.title('Traffic Light-Automatic')
play.configure(bg='Lightblue')

Button(play, text='start', font=('calibri',15), bg='gray',fg='white', width='8', height='2', command=start).place(x=20,y=30)

timeinterval=Label(play, font=('calibri',30,'bold'), bg='black', fg='red')
timeinterval.place(x=20, y=200)

canvas1=Canvas(play, height=130, bg='black',width=130)
canvas1.place(x=130, y=30)
canvas2=Canvas(play, height=130, bg='black',width=130)
canvas2.place(x=130, y=165)
canvas3=Canvas(play, height=130, bg='black',width=130)
canvas3.place(x=130, y=300)

play.mainloop()