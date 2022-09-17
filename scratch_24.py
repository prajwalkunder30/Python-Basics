from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x350")
root.title("Slider tutorial")
def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank")
    tmsg.showinfo("Amount Credited",f"We have credited {myslider2.get()} dollar")
myslider=Scale(root,from_=0,to=455)
myslider.pack()
Label(root,text="HOW MANY DOLLARS DO YOU WANT?").pack()
myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.pack()
Button(root,text="Get dollars",command=getdollar).pack()
root.mainloop()