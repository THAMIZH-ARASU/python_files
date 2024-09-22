from tkinter import *
import tkMessageBox
master=Tk()
num=StringVar()

def callme():
    if int(num.get())<0:
        tkMessageBox.showinfo("Error","Enter a Positive number")
    else:
        tkMessageBox.showinfo("Welcome","Valid Number!")
Label(master,text="Enter a number:").pack()

Entry(master,textvariable=num).pack()
B=Button(master,text="Submit",command=callme)
B.pack()
mainloop()
