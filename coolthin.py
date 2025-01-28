# Author : Levi Yates
# Date   : 2022-11-26
# This program is a translator to piglatin.


import tkinter

def scram():
    print("I am in translation function!")
    myString = entInput.get()
    user_word = myString

    first_letter = user_word[0]
    first_letter = str(first_letter)
    first_letter=first_letter.upper()


    ay = 'ay'
    way = 'way'
    consonant = ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','Y','V','X','Z')
    vowel = ('A','E','I','O','U')
    
    if first_letter in consonant:
    
        print(first_letter,'is a consonant')
        length_of_word = len(user_word)
        remove_first_letter = user_word[1:length_of_word]
        pig_latin=remove_first_letter+first_letter+ay
        print('The word in Pig Latin is:',pig_latin)
        
    elif first_letter in vowel:
    
        print(first_letter,'is a vowel')
        pig_latin = user_word + way
        
    else:
    
        print('I dont know what' + first_letter + 'is')
        pig_latin = 'UNKNOWN'

    entOutput.delete(0, tkinter.END)
    entOutput.insert(0, pig_latin)



# getting first letter and making sure its a string and setting it to uppercase



root = tkinter.Tk()
print("See, I can still print to our shell window.")
root.title("Piglatin Translator")
root.geometry("250x200")

lblDirections = tkinter.Label(root, text="Enter some text to be translated to Pig Latin!")
entInput = tkinter.Entry(root)
btnScramble = tkinter.Button(root, text="Enter a word to translate to Pig Latin",
                             fg="#0000FF", bg="#CCCCCC", command=scram)
entOutput = tkinter.Entry(root)
lblCredits = tkinter.Label(root, text="\u00A9 Levi Yates")


lblDirections.grid(padx=5, pady=5)
entInput.grid(padx=5, pady=5)
btnScramble.grid(padx=5, pady=5)
entOutput.grid(padx=5, pady=5)
lblCredits.grid(padx=5, pady=5)
                




root.mainloop()
