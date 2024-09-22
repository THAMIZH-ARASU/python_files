from tkinter import *
master=Tk()
v=StringVar()
w=Label(master,textvariable=v,fg="red",font=("Verdana",14),anchor=W,justify=CENTER)
v.set("Labels can display multiple lines of text.\n\
You can use new lines or use wraplength option\n\
to mae the Label wrap text by itself.")
w.pack()
print(v.get())
mainloop()
