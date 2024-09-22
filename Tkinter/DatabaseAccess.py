from tkinter import *
import MySQLdb

#Open database connection
db=MySQLdb.connect("127.0.0.1","root","","cscdata")
#prepare a cursor object cursor() method

cursor=db.cursor()
master=Tk()

group=LabelFrame(master,text=" EMPOYEE DATA ENTRY SCREEN ",padx=10,pady=10)

t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
c1=StringVar()

tsex=StringVar()

def callme():
    if c1.get()=="M":
        tsex="Male"
    else:
        tsex="Female"
    sql="insert into cscemp(empno,empname,sex,desig,salary)\
    values('%d','%s','%s','%s','%f')"%(int(t1.get()),t2.get(),t3.get(),float(t4.get()))
    cursor.execute(sql)
    db.commit()

Label(group,text="Employee No:").grid(row=0,column=3)
w=Entry(group,textvariable=t1).grid(row=0,column=20)
Label(group,text="Employee Name:").grid(row=2,column=3)
w1=Entry(group,textvariable=t2).grid(row=2,column=20)
Label(group,text="designation:").grid(row=6,column=3)
w3=Entry(group,textvariable=t3).grid(row=6,column=20)
Label(group,text="Sex:").grid(row=4,column=3)
r1=Radiobutton(group,text="Male",variable=c1,value="M").grid(row=4,column=20)
r2=Radiobutton(group,text="Female",variable=c1,value="F").grid(row=4,column=25)
b1=Button(group,text="ADD",command=callme).grid(row=7,column=25)
w4=Entry(group,textvariable=t4).grid(row=8,column=20)
Label(group,text="Salary:").grid(row=8,column=3)
c1.set("M")

mainloop()
db.close()
