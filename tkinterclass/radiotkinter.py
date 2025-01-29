from tkinter import *
root = Tk()
root.geometry('400x400')
def add():
    # print(var.get())
    c = 'you selected ' + var.get()
    lbl.config(text=c)

ioe = {'ram':1200,'shyam':2300}
print(ioe.items())
for key,v in ioe.items():
    label = Label(text=key+str(v))
    label.pack()

var = StringVar()
r1 = Radiobutton(root, text='Male',variable=var,value='Male',command=add)
r1.pack(anchor=NW)
r2 = Radiobutton(root, text='Female',variable=var,value='Female',command=add)
r2.pack(anchor=N)
r3 = Radiobutton(root, text='Other',variable=var,value='Other',command=add)
r3.pack(anchor=NE)
# var = IntVar()
# r1 = Radiobutton(root, text='Male',variable=var,value=1,command=add)
# r1.pack(anchor=W)
# r2 = Radiobutton(root, text='Female',variable=var,value=2,command=add)
# r2.pack(anchor=W)
# r3 = Radiobutton(root, text='Other',variable=var,value=3,command=add)
# r3.pack(anchor=W)
lbl = Label()
lbl.pack(anchor=W)

root.mainloop()


