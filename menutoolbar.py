# Author : Levi Yates
# Date   : 2022-11-28
# Examples of a menu bar

import os
import platform
import tkinter
import tkinter.messagebox

def mnuNewFile():
    print("New File Created")

def mnuSave():
    print("Saved File")

def mnuExit():
    print("Exited File")
    answer = tkinter.messagebox.askquestion("Confirmation",
                                            "Are you sure you want to exit?",
                                            default='no')
    if answer == "yes" :
        root.destroy()
    
def mnuProgHelp():
    print("Program Help pressed...")


# Program execution starts here...
# Create and build our screen

root = tkinter.Tk()
root.title("Printing Program")
root.geometry("500x300") # That goes by Width x Length
                    
print("os = " + os.name)
print("platform system = " + platform.system())
print("platform release = " + platform.release())

# Display icon only if on Windows
if  platform.system() == "Windows" :
     root.iconbitmap("monstersalien.ico")

# Create the menu
myMenu = tkinter.Menu(root)
root.config(menu=myMenu)

mnuFile = tkinter.Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="File", menu=mnuFile)
mnuFile.add_command(label="New File", command=mnuNewFile,
                    accelerator="Ctrl+N")
root.bind_all("<Control-n>", lambda event: root.after(100, mnuNewFile))
mnuFile.add_command(label="Save", command=mnuSave,
                    accelerator="Ctrl+S")
root.bind_all("<Control-s>", lambda event: root.after(100, mnuSave))
mnuFile.add_command(label="Exit", command=mnuExit,
                    accelerator="Ctrl+X")
root.bind_all("<Control-x>", lambda event: root.after(100, mnuExit))

mnuHelp = tkinter.Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Help", menu=mnuHelp)
mnuHelp.add_command(label="Program Help", command=mnuProgHelp)



lblCredits = tkinter.Label(root, text="\u00A9 Levi Yates")

lblCredits.grid(padx=5, pady=5)

root.mainloop()

# End of program

