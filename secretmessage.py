# Author : Levi Yates
# Date   : 2022-11-21
# This program is derived from the original shell application
# called strinmanip.py. This program uses the TKinter GUI.

#from tkinter import *
import tkinter

def scram():
    print("I am in scram function...")
    myString = entInput.get()
    #print("This is what was in the entry box: " + myString)

    scrambletable = ''.maketrans('abcdefghijklmnopqrstuvwxyz',
                                 'zyxwvutsrqponmlkjihgfedcba')

    scramble = myString.translate(scrambletable)
    #print("Scrambled Successfully! " + scramble)

    entOutput.delete(0, tkinter.END)
    entOutput.insert(0, scramble)
    # End of function scram



# Program execution starts here...
# Create and build our screen

root = tkinter.Tk()
print("See, I can still print to our shell window.")
root.title("Scramble / Descamble")
root.geometry("235x200")

lblDirections = tkinter.Label(root, text="Enter some text to be egg-scrambled!")
entInput = tkinter.Entry(root)
btnScramble = tkinter.Button(root, text="Scramble your Eggs!",
                             fg="#0000FF", bg="#CCCCCC", command=scram)
entOutput = tkinter.Entry(root)
lblCredits = tkinter.Label(root, text="\u00A9 Levi Yeets, 1965")


lblDirections.grid(padx=5, pady=5)
entInput.grid(padx=5, pady=5)
btnScramble.grid(padx=5, pady=5)
entOutput.grid(padx=5, pady=5)
lblCredits.grid(padx=5, pady=5)
                    

root.mainloop()

# End of program
