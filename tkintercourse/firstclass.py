from tkinter import *

root = Tk()
# GUI Logic
# geometry takes widthxheight
root.geometry("700x500")

# min or max size takes width, height
root.minsize(200,100)
root.maxsize(1200,700)

labeltext = Label(text='Good luck')
labeltext.pack()

root.mainloop()