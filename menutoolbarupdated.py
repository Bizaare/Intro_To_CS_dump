# Author : Levi Yates
# Date   : 2022-11-28
# Examples of a menu bar

import os
import platform
import tkinter
import tkinter.messagebox
import time
import threading

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

def cmdCut():
    print("File Contents Cut")

def cmdCopy():
    print("File Contents Copied")

def cmdPaste():
    print("File Contents Pasted")

def mouseMotion(event):
    x,y = event.x, event.y
    statusText.set('x={}, y={}' . format(x,y))
    greenCircle = myCanvas.create_oval(
        x-7, y-7, x+7, y+7, fill="green")
def repeatingLoop():
    if threadsRun:
        statusTextR.set(time.ctime())
        threading.Timer(1, repeatingLoop).start()

# Program execution starts here...
# Create and build our screen

root = tkinter.Tk()
root.title("Printing Program")
# Size of window has to be taller for windows machines
#if os.name == "nt":
    #root.geometry("400x396") # That goes by Width x Length
#else:
root.geometry("400x391")
                    
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

# Create a Toolbar
toolbar = tkinter.Frame(root, bg="gray")

btnCut = tkinter.Button(toolbar, command=cmdCut)
btnCutIcon = tkinter.PhotoImage(file="cut.gif")
btnCut.config(image=btnCutIcon, width=36, height=36)
btnCut.pack(side=tkinter.LEFT, padx=2, pady=2)

btnCopy = tkinter.Button(toolbar, command=cmdCopy)
btnCopyIcon = tkinter.PhotoImage(file="copy.gif")
btnCopy.config(image=btnCopyIcon, width=36, height=36)
btnCopy.pack(side=tkinter.LEFT, padx=2, pady=2)

btnPaste = tkinter.Button(toolbar, command=cmdPaste)
btnPasteIcon = tkinter.PhotoImage(file="paste.gif")
btnPaste.config(image=btnPasteIcon, width=36, height=36)
btnPaste.pack(side=tkinter.LEFT, padx=2, pady=2)

toolbar.grid(row=0, column=0, columnspan=2,
             sticky=tkinter.W+tkinter.E)


# Create a status Bar
statusText = tkinter.StringVar()
statusText.set("Program loading")
statusBar = tkinter.Label(root, textvariable=statusText,
                          bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W)
statusBar.grid(row=3, column=0, sticky=tkinter.W+tkinter.E)

statusTextR = tkinter.StringVar()
statusTextR.set("Right Side")
statusBarR = tkinter.Label(root, textvariable=statusTextR,
                          bd=1, relief=tkinter.SUNKEN, anchor=tkinter.E)
statusBarR.grid(row=3, column=1, sticky=tkinter.W+tkinter.E)

# Create a Canvas
myCanvas = tkinter.Canvas(root, width=395, height=280, bg="aliceblue")
myCanvas.grid(row=1, column=0, columnspan=2)

blueline = myCanvas.create_line(5,80, 400, 65, fill="blue")
greenline = myCanvas.create_line(0,100, 200, 50, fill="green")
greenbox = myCanvas.create_rectangle(180,180, 440, 20, fill="orange")
crossOne = myCanvas.create_line(100,50, 100, 150)
crossTwo = myCanvas.create_line(27,70, 170, 70)

yellowtriangle = myCanvas.create_polygon(275,0, 225,200, 325,200, fill="yellow")
myCanvas.create_oval(
        70, 60, 120, 90, fill="green")
myCanvas.create_oval(
        40, 60, 80, 120, fill="white")
myCanvas.create_oval(
        20, 20, 50, 300, fill="yellow")
myCanvas.create_oval(
        220, 200, 210, 230, fill="blue")


hiText = myCanvas.create_text(250,200,
    text="Hello There", font=('Helvetica', 12), fill="Black")
idkText = myCanvas.create_text(200, 260, text="I do not know what to make.",
                               fill="Blue")

# Bind the mouse motion event
root.bind('<Button 1>', mouseMotion)

lblCredits = tkinter.Label(root, text="\u00A9 Levi Yates")

lblCredits.grid(row=2, column=1, sticky=tkinter.E)



# Start the repeating Timer
threadsRun = True
repeatingLoop() 

root.mainloop()

# Main Screen/program thread end
# Shut down all thread
threadsRun = False

print("End of progam")

# End of program

