from tkinter import *

root=Tk()

def Open():
    print("Opened!")

def Save():
    print("Saved!")

def Cut():
    print("Cut!")

def Copy():
    print("Copied!")

def Paste():
    print("Pasted!")

def Help():
    print("Helped!")

def About():
    print("About:")
    print("     PullDown Menu with TKinter...!")
    print("Author:  Thamizharasu")

def Exit():
    print("EXITED!!!!!!!")
    root.quit()
    
menubar=Menu(root)

#create a pulldown menu, and ad it to the menu bar

filemenu=Menu(menubar,tearoff=0)

filemenu.add_command(label="Open",command=Open)
filemenu.add_command(label="Save",command=Save)
filemenu.add_separator()

filemenu.add_command(label="Exit",command=Exit)
menubar.add_cascade(label="File",menu=filemenu)

#create more pulldown menus

editmenu=Menu(menubar,tearoff=0)

editmenu.add_command(label="Cut",command=Cut)
editmenu.add_command(label="Copy",command=Copy)
editmenu.add_command(label="Paste",command=Paste)

menubar.add_cascade(label="Edit",menu=editmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Help",command=Help)
helpmenu.add_command(label="About",command=About)
menubar.add_cascade(label="Help",menu=helpmenu)

#displaying the menu

root.config(menu=menubar)


mainloop()
