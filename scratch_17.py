from tkinter import *
from PIL import Image, ImageTk


mahmudul_root = Tk()
pk=Label(text="WELCOME TO TELUSKO")
pk.pack()

mahmudul_root.geometry("1255x944")
image=Image.open("pkk.jpg")
photo=ImageTk.PhotoImage(image)
pj=Label(image=photo)
pj.pack()
punit=Label(text="WELCOME PUNIT")
punit.pack()

mahmudul_root.mainloop()