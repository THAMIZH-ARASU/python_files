#Simple GUI Calculator ...

#importing the required tkinter module
import tkinter as tk


fieldText=""     #setting a nul text field value

def add_to_field(sth):
    global fieldText
    fieldText+=str(sth)
    field.delete("1.0","end")
    field.insert("1.0",fieldText)

#function to display the result on the text field 
def calculate():
    global fieldText
    result=str(eval(fieldText))
    field.delete("1.0","end")
    field.insert("1.0",result)

# function to clear the text field
def clear():
    global fieldText
    fieldText=""
    fieldText.delete("1.0","end")

master=tk.Tk()
master.geometry("300x300")
field=tk.Text(master,height=2,width=21,font=("Time New Roman",20))
field.grid(row=1,column=1,columnspan=4)

#Number Buttons
b1=tk.Button(master,text="1",command=lambda:add_to_field(1),width=5,font=("Times New Roman",14))
b1.grid(row=4,column=1)

b2=tk.Button(master,text="2",command=lambda:add_to_field(2),width=5,font=("Times New Roman",14))
b2.grid(row=4,column=2)

b3=tk.Button(master,text="3",command=lambda:add_to_field(3),width=5,font=("Times New Roman",14))
b3.grid(row=4,column=3)

b4=tk.Button(master,text="4",command=lambda:add_to_field(4),width=5,font=("Times New Roman",14))
b4.grid(row=3,column=1)

b5=tk.Button(master,text="5",command=lambda:add_to_field(5),width=5,font=("Times New Roman",14))
b5.grid(row=3,column=2)

b6=tk.Button(master,text="6",command=lambda:add_to_field(6),width=5,font=("Times New Roman",14))
b6.grid(row=3,column=3)

b7=tk.Button(master,text="7",command=lambda:add_to_field(7),width=5,font=("Times New Roman",14))
b7.grid(row=2,column=1)

b8=tk.Button(master,text="8",command=lambda:add_to_field(8),width=5,font=("Times New Roman",14))
b8.grid(row=2,column=2)

b9=tk.Button(master,text="9",command=lambda:add_to_field(9),width=5,font=("Times New Roman",14))
b9.grid(row=2,column=3)

b0=tk.Button(master,text="0",command=lambda:add_to_field(0),width=5,font=("Times New Roman",14))
b0.grid(row=5,column=1)

#Buttons for doing Operations

badd=tk.Button(master,text="+",command=lambda:add_to_field("+"),width=5,font=("Times New Roman",14))
badd.grid(row=4,column=4)

bsub=tk.Button(master,text="-",command=lambda:add_to_field("-"),width=5,font=("Times New Roman",14))
bsub.grid(row=5,column=4)

bmul=tk.Button(master,text="x",command=lambda:add_to_field("x"),width=5,font=("Times New Roman",14))
bmul.grid(row=3,column=4)

bdiv=tk.Button(master,text="/",command=lambda:add_to_field("/"),width=5,font=("Times New Roman",14))
bdiv.grid(row=2,column=4)

bclr=tk.Button(master,text="C",command=lambda:clear(),width=5,font=("Times New Roman",14))
bclr.grid(row=5,column=3)

bdec=tk.Button(master,text=".",command=lambda:add_to_field("."),width=5,font=("Times New Roman",14))
bdec.grid(row=5,column=2)

bOpenParanthesis=tk.Button(master,text="(",command=lambda:add_to_field("("),width=5,font=("Times New Roman",14))
bOpenParanthesis.grid(row=6,column=1)

bCloseParanthesis=tk.Button(master,text=")",command=lambda:add_to_field(")"),width=5,font=("Times New Roman",14))
bCloseParanthesis.grid(row=6,column=2)

beq=tk.Button(master,text="=",command=lambda:calculate(),width=5,font=("Times New Roman",14))
beq.grid(row=6,column=3,columnspan=2)

master.mainloop()