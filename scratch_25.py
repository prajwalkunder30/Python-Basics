from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("455x450")
# def order():
#     tmsg.showinfo("Order Received",f"We have received your order for {var.get()} ,thanks for ordering" )
# var=IntVar()
# Label(root,text="What would you like to have?",justify=LEFT,font="lucida 19 bold",padx=14).pack()
# radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value=1).pack(anchor="w")
# radio=Radiobutton(root,text="Idli",padx=14,variable=var,value=2).pack(anchor="w")
# radio=Radiobutton(root,text="Sambhar",padx=14,variable=var,value=3).pack(anchor="w")
# radio=Radiobutton(root,text="Vadapav",padx=14,variable=var,value=4).pack(anchor="w")
# Button(text="Order Now",command=order).pack()
var=IntVar()
var1=StringVar()
def myfunc():
    tmsg.showinfo("Your selection",f"You live in {var.get()} city")
Label(text="Which city do you live in?",font="lucida 19 bold",padx=14,justify=LEFT).pack()
radio=Radiobutton(root,text="Mumbai",padx=14,variable=var,value=1).pack(anchor="w")
radio=Radiobutton(root,text="Delhi",padx=14,variable=var,value=2).pack(anchor="w")
radio=Radiobutton(root,text="Chennai",padx=14,variable=var,value=3).pack(anchor="w")
radio=Radiobutton(root,text="Bengaluru",padx=14,variable=var,value=4).pack(anchor="w")
Button(root,text="Submit Now",command=myfunc).pack()
root.mainloop()