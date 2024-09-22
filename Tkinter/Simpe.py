from tkinter import *
root=Tk()

def hello():
    print("hello")

#creating a toplevel menu

menubar=Menu(root)
menubar.add_command(label="hello!",command=hello)
menubar.add_command(label="Quit!",command=root.quit)

#displaying the menu

root.config(menu=menubar)
mainloop()

