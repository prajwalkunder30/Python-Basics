from tkinter import *
root=Tk()
root.geometry("600x200")
def getvals():
    root.geometry(f"{iwwvalue.get()}x{iwhvalue.get()}")


pk=Label(root,text="WELCOME TO GUI WINDOW RESIZER",font="comicsansms 13 bold").grid(row=0,column=3)
iwidget_width=Label(root,text="ENTER INPUT WIDTH").grid(row=1,column=1)
iwidget_height=Label(root,text="ENTER INPUT HEIGHT").grid(row=2,column=1)
iwwvalue=IntVar()
iwhvalue=IntVar()
iwwentry=Entry(root,textvariable=iwwvalue).grid(row=1,column=2)
iwhentry=Entry(root,textvariable=iwhvalue).grid(row=2,column=2)
Button(text="Apply",command=getvals).grid(row=3,column=3)

root.mainloop()