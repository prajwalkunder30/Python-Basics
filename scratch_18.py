from tkinter import *
from PIL import Image, ImageTk

pk_root=Tk()

label=Label(text="WELCOME TO PRAJWAL NEWS")
label.pack()
photo = PhotoImage(file="1.png")
pk = Label(image=photo)
pk.pack()
txt=open("1.txt","rb")
txt.close()
lab=Label(text=txt)
lab.pack()
pk_root.mainloop()
