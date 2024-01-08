from tkinter import *
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

play = Tk()
play.geometry('300x450')
play.title('Traffic Lighths- Manual')
play.configure(bg='Lightblue')

Button(play, bg='red', width='8', height='2',command=red).place(x=20, y=30)
Button(play, bg='orange', width='8', height='2',command=orange).place(x=20, y=130)
Button(play, bg='green', width='8', height='2',command=green).place(x=20, y=230)

canvas1=Canvas(play, height=130, bg='black',width=130)
canvas1.place(x=130, y=30)
canvas2=Canvas(play, height=130, bg='black',width=130)
canvas2.place(x=130, y=165)
canvas3=Canvas(play, height=130, bg='black',width=130)
canvas3.place(x=130, y=300)

play.mainloop()