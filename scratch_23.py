from tkinter import *
root=Tk()
root.geometry("500x500")
def Newp():
    print("This is your New Project")
mainmenu=Menu(root)
m1=Menu(mainmenu)
m1.add_command(label="New Project",command=Newp)
m1.add_command(label="Save")
m1.add_separator()
m1.add_command(label="Save As")
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)
m2=Menu(mainmenu)
m2.add_command(label="Cut",command=Newp)
m2.add_command(label="Copy")
m2.add_separator()
m2.add_command(label="Paste")
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

root.mainloop()