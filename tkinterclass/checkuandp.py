from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400')

def check():
    default_u = 'admin'
    default_p = 'password'
    if e_username.get() == default_u and e_password.get() == default_p:
        messagebox.showinfo(title='Congratulations',message='You are successfully logged in')
    else:
        messagebox.showerror('Error in Login',message='Incorrect Username or Passowrd')
        

l_username = Label(text='Username')
l_password = Label(text='Password')

e_username = Entry()
e_password = Entry(show='*')

btn_login = Button(text='Login', command=check)

l_username.pack()
e_username.pack()
l_password.pack()
e_password.pack()
btn_login.pack()

mainloop()