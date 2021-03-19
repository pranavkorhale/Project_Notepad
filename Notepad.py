from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
import sys
import re



def newfile():
    global file
    root.title("untitled notepad")
    file = None
    TextArea.delete(1.0,END)   #from 1 st line of zeroth character all are remove


def openFile():
    global  file
    file = asksaveasfilename(defaultextension=".text",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file = None
    else:
        root.title(os.path.basename(file)+" NOTEPAD")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("About","This notepad is created by Korhale Pranav from India")
def rateus():
    rtus = mb.askquestion("Rate us !","Do you like our app")
    if rtus == "yes":
        showinfo("Thank you very much","stay tunned for more updates...")
    else:
        showinfo("sorry for this","Our customer executive contact you soon......")
def contact():
    showinfo("Contact us", "If you face any difficulty then feel free to aks our phonno:XXXXXXXXX or email us on: xxx@_.com ")




if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad    --Handcrafted in India  By KORHALE PRANAV")

    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)


    MenuBar = Menu(root)


    FileMenu = Menu(MenuBar, tearoff=0)

    FileMenu.add_command(label="New", command=newfile)

    FileMenu.add_command(label="Open", command = openFile)



    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)
    # EditMenu.add_command(label= "Find",command=find)
    MenuBar.add_cascade(label="Edit", menu = EditMenu)



    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="Contact support",command=contact)
    HelpMenu.add_command(label = "About Notepad", command=about)

    MenuBar.add_cascade(label="Help", menu=HelpMenu)


    Rateus = Menu(MenuBar,tearoff=0)
    Rateus.add_command(label="Rate us", command=rateus)
    MenuBar.add_cascade(label="Rate us",menu=Rateus)
    root.config(menu=MenuBar)


    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()