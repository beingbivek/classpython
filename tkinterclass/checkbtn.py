from tkinter import *

root = Tk()
def add():
    c=str(CheckVar1.get()) + str(CheckVar2.get()) + str(CheckVar3.get()) + str(CheckVar4.get())
    label.config(text=c)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

C1 = Checkbutton(root,text='Music',variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20)
C2 = Checkbutton(root,text='Sports',variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20)
C3 = Checkbutton(root,text='Youtube',variable=CheckVar3,onvalue=1,offvalue=0,height=5,width=20)
C4 = Checkbutton(root,text='Dance',variable=CheckVar4,onvalue=1,offvalue=0,height=5,width=20)

C1.pack()
C2.pack()
C3.pack()
C4.pack()
btn = Button(root, text="Click",command=add)
label = Label(root)
label.pack()
btn.pack()

root.mainloop()