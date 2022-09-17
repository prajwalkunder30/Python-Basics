from tkinter import *
root=Tk()
root.geometry("655x333")
f1=Frame(root,bg="grey",relief=SUNKEN)

f1.pack(side=LEFT,fill="y")
f2=Frame(root,bg="grey",relief=SUNKEN)

f2.pack(side=TOP,fill="x")
f3=Frame(root,bg="grey",relief=SUNKEN)

f3.pack(side=RIGHT,fill="y")
f4=Frame(root,bg="grey",relief=SUNKEN)

f4.pack(side=BOTTOM,fill="x")

def hello():
    print("HELLO MY NAME IS PRAJWAL")
def age():
    print("HELLO MY AGE IS 18")
def place():
    print("HELLO I LEAVE IN MUMBAI")
def rollno():
    print("HELLO MY ROLL NO  IS 24")
b1=Button(f1,fg="red",text="Print Now",command=hello)
b1.pack()
b2=Button(f2,fg="red",text="Print Now",command=age)
b2.pack()
b3=Button(f3,fg="red",text="Print Now",command=place)
b3.pack()
b4=Button(f4,fg="red",text="Print Now",command=rollno)
b4.pack()
root.mainloop()
