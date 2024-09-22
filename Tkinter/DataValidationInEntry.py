from tkinter import *
master=Tk()
l=Label(master,text="Enter a number:",justify=LEFT)
e=Entry(master)
l.pack()
e.pack()
e.focus_set()
def callback():
    if int(e.get())<0:
        print("Must be positive.")
        e.delete(0,END)
        e.focus_set()
b=Button(master,text="GET",width=10,command=callback)
b.pack()
mainloop()
