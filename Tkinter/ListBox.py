from tkinter import *
master=Tk()
txt=StringVar()
listbox=Listbox(master)
listbox.pack()
for item in ["HDCA","HDCP","ADJP","J2EE","DCA"]:
    listbox.insert(END,item)

def callback():
    txt.set(listbox.get(ACTIVE))

Label(master,text="Selected Item:").pack()
Entry(master,text=" ",textvariable=txt).pack()
button=Button(master,text="PRESS ME",command=callback)
button.pack()

mainloop()
