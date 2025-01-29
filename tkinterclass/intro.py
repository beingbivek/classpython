from tkinter import *

# window = Tk()
# window.title('Login')
# window.iconbitmap(r'D:\Bivek Study Files\Python Coding\tkinterclass\login.ico')
# window.geometry('600x600')
# window.resizable(0,0) # resizable 0 will fix the length and breadth while 1 can change it

# Button(text='Login')
'''
pack-default top centre,need sides for eg, LEFT,RIGHT
grid-default top left,needs value in row and column
place-always have to insert x,y cordinates
'''

root = Tk()
# root.geometry('200x200')

# redbutton = Button(root, text='LEFT', fg = 'green')
# # redbutton.pack(side=LEFT)
# redbutton.grid()

# greenbutton = Button(root, text='RIGHT', fg = 'black')
# greenbutton.pack(side=RIGHT)

# bluebutton = Button(root, text='TOP', fg = 'blue')
# bluebutton.pack(side=TOP)

# blackbutton = Button(root, text='BOTTOM', fg = 'red')
# blackbutton.pack(side=BOTTOM)

# name = Label(root,text="Name").grid(row=0,column=0)
# e1 = Entry(root).grid(row = 0,column=1)

# password = Label(root,text="Password").grid(row=1,column=0)
# e2 = Entry(root).grid(row = 1,column=1)

# submit = Button(root, text='Submit').grid(row=4,column=1)

root.geometry('400x250')
name = Label(root,text="Name").place(x=30,y=50)
address = Label(root,text="Address").place(x=30,y=90)
contact = Label(root,text="Contact").place(x=30,y=130)
e1 = Entry(root).place(x=80,y=50)
e2 = Entry(root).place(x=80,y=90)
e3 = Entry(root).place(x=95,y=130)


mainloop()