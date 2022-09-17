from tkinter import*
root=Tk()
root.title("A simple Calculator")
root.geometry("800x200")
def add():
    anvalue=f"{fnvalue.get()+snvalue.get()}"
    lab=Label(root,text=anvalue).grid(row=10,column=1)




def sub():
    anvalue = f"{fnvalue.get() - snvalue.get()}"
    lab=Label(root,text=anvalue).grid(row=10,column=1)


def mul():
    anvalue = f"{fnvalue.get() * snvalue.get()}"
    lab=Label(root,text=anvalue).grid(row=10,column=1)


def div():
    anvalue = f"{fnvalue.get() / snvalue.get()}"
    lab = Label(root, text=anvalue).grid(row=10, column=1)


label=Label(root,text="A SIMPLE HUMAN CALCULATOR",font="lucida 10 bold").grid(row=0,column=3)
lab=Label(root,text="ENTER FIRST NO").grid(row=1,column=0)
lab=Label(root,text="ENTER SECOND NO").grid(row=2,column=0)
fnvalue=IntVar()
snvalue=IntVar()
fnentry=Entry(root,textvariable=fnvalue).grid(row=1,column=1)
snentry=Entry(root,textvariable=snvalue).grid(row=2,column=1)
Button(root,text="ADDITION",command=add).grid(row=4,column=0)
Button(root,text="SUBTRACTION",command=sub).grid(row=4,column=1)
Button(root,text="MULTIPLICATION",command=mul).grid(row=4,column=2)
Button(root,text="DIVISION",command=div).grid(row=4,column=3)

Label(root, text="ANSWER").grid(row=10, column=0)

root.mainloop()