from tkinter import *
master=Tk()
sptxt=StringVar()
sptxt.set("DMO")
def callme():
    print(sptxt.get())

w=Spinbox(master,textvariable=sptxt,values=("HDCA","HDCP","ADJP","DCA","J2EE","DTP"),fg="green",command=callme,bd=4)
sptxt.set("DCA")

w.pack()
mainloop()
