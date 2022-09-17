from tkinter import *
def Newfile():
    pass
def Openfile():
    pass
def Savefile():
    pass
def cut():
    pass
def copy():
    pass
def paste():
    pass
def about():
    pass

if __name__=='__main__':
    root=Tk()
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("644x788")
    textarea=Text(root,font="lucida 19 bold")
    file=None
    textarea.pack(expand=True,fill=BOTH)
    MenuBar=Menu(root)
    FileMenu=Menu(MenuBar,tearoff=0)
    FileMenu.add_command(label="New",command=Newfile)
    FileMenu.add_command(label="Open",command=Openfile)
    FileMenu.add_command(label="Save",command=Savefile)
    FileMenu.add_separator()
    MenuBar.add_cascade(label="File",menu=FileMenu)
    EditMenu=Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    root.config(menu=MenuBar)
    scrollbar=Scrollbar(textarea)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)







    root.mainloop()