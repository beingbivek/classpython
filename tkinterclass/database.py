from tkinter import *
import sqlite3
 
root = Tk()
 
 
conn = sqlite3.connect('python.db') #database creation
 
c = conn.cursor() # neded before commanding sqldatbase
c.execute('''CREATE TABLE IF NOT EXISTS happy(
          f_name text,
          l_name text)''') # fanem and l_name column ho
 
conn.commit() #commit changes in database permanently
 
conn.close() #closes database
 
def add():
    conn = sqlite3.connect('python.db') #database craetion
 
    c = conn.cursor() # before commanding datbase
    c.execute('INSERT INTO happy VALUES(?,?)',(e1.get(), e2.get())) # ? is placeholder which is there to put values by inserting method
 
 
    conn.commit() #commit changes in database permanently
 
    conn.close() #closes database
    e1.delete(0,END)
    e2.delete(0,END)
 
 
def show():
    conn = sqlite3.connect('python.db')
    c = conn.cursor() # before commanding datbase
    c.execute('SELECT *, oid FROM happy') # oid = object id, * = all
    result = c.fetchall()
    #print(results)
    #lbl.config(text=results)
    results = ''
 
    for record in result:
        results += record[0] + ' '+ record[1]  + str(record[2]) + '\n' # record[0] = f_name and record[1]= l_name and str(record[2]) = shows obejct id at last for us
        lbl.config(text=results)
 
 
def delete():
     conn = sqlite3.connect('python.db') #database craetion
 
     c = conn.cursor() # before commanding datbase
     c.execute('DELETE FROM happy WHERE oid=' +  e3.get())
     conn.commit()
     conn.close()
 
 
def edit():
    global roots
    global e4
    global e5
    roots = Toplevel()
    e4 = Entry(roots,)
    e4.pack()
    e5 = Entry(roots,)
    e5.pack()
    btn5= Button(roots, text= 'Save',command=update)
    btn5.pack()
    conn = sqlite3.connect('python.db')
    c = conn.cursor() # before commanding datbase
    c.execute('SELECT * FROM happy WHERE oid= ' +e3.get()) # oid = object id, * = all
    result = c.fetchall()
    for i in result:
        e4.insert(0,i[0])
        e5.insert(0,i[1])
 
def update():
    conn = sqlite3.connect('python.db')
    c = conn.cursor()
    c.execute("""UPDATE happy SET
              f_name = :a,
              l_name = :b
              WHERE oid= :oid
        """,
        {
            'a' : e4.get(),
            'b' : e5.get(),
            'oid' :e3.get()
        }
    )
    conn.commit()
    conn.close()
    roots.destroy()
   
 
 
 
 
 
 

 
 
 
e1= Entry(root, width = 30)
e1.pack()
 
e2= Entry(root, width = 30)
e2.pack()
 

 
 
 
btn = Button(root, text= 'Button', command=add)
btn.pack()
 
btn2 = Button(root, text= 'Show', command=show)
btn2.pack()
 
btn3 = Button(root, text = 'Delete', command = delete)
btn3.pack()
 
 
btn4 = Button(root, text = 'Edit', command = edit)
btn4.pack()
 
e3= Entry(root, width = 30)
e3.pack()
 
 
lbl = Label(text='')
lbl.pack()
 
 
mainloop()