from tkinter import *

def login():
    root = Toplevel()
    root.geometry('400x200')

    name = Label(root,text="Name").grid(row=0,column=0)
    e1 = Entry(root).grid(row = 0,column=1)

    password = Label(root,text="Password").grid(row=1,column=0)
    e2 = Entry(root).grid(row = 1,column=1)

    submit = Button(root,text='Submit').grid(row=3,column=0)

def registration():
    root = Toplevel()
    root.geometry('500x400')
    def on_entry_click(root,e5):
        if e5.get() == "Enter your text here":
            e5.delete(0, END) 
            
    def on_focusout(root,e5):
        if e5.get() == '': 
            e5.insert(0, "Enter your text here")

    name = Label(root,text="Name").grid(row=0,column=0)
    e1 = Entry(root).grid(row = 0,column=1)

    email = Label(root,text="Email").grid(row=1,column=0)
    e2 = Entry(root).grid(row = 1,column=1)

    phone = Label(root,text="Phone").grid(row=2,column=0)
    e3 = Entry(root).grid(row = 2,column=1)

    password = Label(root,text="Password").grid(row=3,column=0)
    e4 = Entry(root).grid(row = 3,column=1)

    confirmpassword = Label(root,text="Confirm Password").grid(row=4,column=0)
    e5 = Entry(root)
    e5.insert(0,'Enter your text here')
    e5.grid(row = 4,column=1)
    e5.bind('<FocusIn>',lambda root:on_entry_click(root,e5))
    e5.bind('<FocusOut>',lambda root:on_focusout(root,e5))

    submit = Button(root,text='Submit').grid(row=6,column=0)

root = Tk()
root.geometry('400x400')

login = Button(root, text='Login',command=login).grid(row=3,column=1)
registration = Button(root, text='Registration',command=registration).grid(row=3,column=2)

mainloop()