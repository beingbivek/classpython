from tkinter import *

root = Tk()
root.geometry('400x400')

def login():
    # abc = ety.get('1.0',END)
    abc = ety.get('2.1','3.2')
    lbl.config(text=abc)

btn = Button(root, text = 'click', command=login)
btn.pack()
ety = Text() # index or each line is start from 1, so for accessing we use float
ety.pack()
lbl = Label(text='')
lbl.pack()

root.mainloop()