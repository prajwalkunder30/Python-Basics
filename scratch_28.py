from tkinter import *
root=Tk()
root.title("PRAJWAL BANK ATM")
root.geometry("800x400")
lab1=Label(text="WELCOME TO PRAJWAL BANK ATM",font="century 25 bold").grid(row=0,column=4)
def balance():
    bal=Tk()
    bal.title("BALANCE")
    bal.geometry("800x400")
    
Button(text="BALANCE",font="arial 15 ",command=balance).grid(row=8,column=0)
Button(text="DEPOSIT",font="arial 15 ",command=deposit).grid(row=12,column=0)
Button(text="WITHDRAW",font="arial 15 ",command=withdraw).grid(row=8,column=4)
Button(text="EXIT",font="arial 15 ",command=quit).grid(row=12,column=4)


root.mainloop()
