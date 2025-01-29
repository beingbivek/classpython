from tkinter import *

root =  Tk()
root.geometry('400x400')

def shuffle():
    if checkvar.get() == 1:
        e.config(show='')
    else:
        e.config(show='*')

checkvar = IntVar()

e = Entry(show='*')
chkbtn = Checkbutton(text='Show password',variable=checkvar,onvalue=1,offvalue=0,command=shuffle)

e.pack()
chkbtn.pack()
mainloop()