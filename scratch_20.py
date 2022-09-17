from tkinter import *
def getvals():
    print(f"THE USERNAME IS {uservalue.get()}")
    print(f"THE PASSWORD IS {passvalue.get()}")


root=Tk()
root.geometry("655x333")
user=Label(root,text="Username")
password=Label(root,text="Password")
user.grid()
password.grid(row=1)
uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(text="Submit",command=getvals).grid()
root.mainloop()