from tkinter import *
master=Tk()
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()

def checkFun():
    txt=StringVar()
    txt=" "
    if var1.get()==1:
        txt=txt+" "+c1.cget("text")
    if var2.get()==1:
        txt=txt+" "+c2.cget("text")
    if var3.get()==1:
        txt=txt+" "+c3.cget("text")
    if var4.get()==1:
        txt=txt+" "+c4.cget("text")
    if var5.get()==1:
        txt=txt+" "+c5.cget("text")
    print(txt)


c1=Checkbutton(master,text="HDCA",variable=var1)
c2=Checkbutton(master,text="HDCP",variable=var2)
c3=Checkbutton(master,text="ADJP",variable=var3)
c4=Checkbutton(master,text="DUC",variable=var4)
c5=Checkbutton(master,text="DCA",variable=var5)

b1=Button(master,text="OK",command=checkFun)

c1.pack()
c2.pack()
c3.pack()
c4.pack()
c5.pack()
b1.pack()

mainloop()
