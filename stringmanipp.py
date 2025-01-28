# Author : Levi Yates
# Date   : 2022-10-10
# Exploration of characters and strings

##print("A")
##print(chr(97))
##print(chr(65))
##print(chr(48))
##
##print(chr(103))
##print(chr(0x67))
##
### East ASian Bopmofo
##print(chr(0x3114))
##
###Print the entire character set
##print()
##for i in ranfe(0x3105, 0x3130):
##    print(chr(i), end=" ")

##print()
###print("C:\users\johndoe\Documents\test.txt")
##print("C:\\users\\johndoe\\Documents\\test.txt")
##
##print()
###print("The quote of the day is "Don't tread on me".")
###print("The quote of the day is "Don't tread on me".')
##print("The quote of the day is \"Don't tread on me\".")
##print("""The quote of the day is "Don't tread on me".""")
##print('The quote of the day is "Don\'t tread on me".')
##
##print()
##print(ord("a"))
##print(ord("A"))
##
##anything = input("Enter a string: ")
##print(anything)
##print(anything.find('s'))
##print("Found " + str(anything.count('s')) + " times.")
##
##if anything.isalnum():
##    print("String contains only letters or numbers")
##else:
##    print("There are special characters in the string.")
##
##
##if anything.isdigit():
##    print("String contains only digits.")
##else:
##    print("There is something other than digits in the string.")
##
##if anything.islower():
##    print("String is all lowercase.")
##else:
##    print("String does not have some uppercase characters in it.")
##
##print()
##print(anything.center(40, " "))
##print(anything.center(40, "*"))
##
##print()
##print(anything.split(" "))
##print(anything.split("s"))
##print(anything.split(" and "))

##anything = input("Enter a string: ")
##print(anything)
##
##### Break a list of number apart that are seperated by commas and space.
####temps = anything.split(", ")
####print(temps)
####print(temps[2])
####print(temps[4])
####print()
##
##newtext = anything.replace("is", "ax")
##print(newtext)
##print()
##
##print(anything[0])
##print(anything[1])
##print(anything[-1])
##print(anything[-2])

##print()
##print(leb(anything))
##

# Check if a password is at least 8 characters long
# and also has at least one uppercase and one lowercase letter.

##goodpwd = True
##password = input("Enter a new password. ")
##
##if len(password) < 8:
##    print("Password is not long enough.")
##    goodpwd = False
##
##if password.islower():
##    print("Password needs at least one upper case letter.")
##    goodpwd = False
##
##if password.isupper():
##    print("Password needs at least one lower case letter.")
##    goodpwd = False
##
##if goodpwd:
##    print("Good password.")
##else:
##    print("Not a good password.")
##
##print()

##import getpass
##
##secret_word = getpass.ggetpass(prompt="Enter your secret word: ")
##print(secret_word)


myString = input("Enter a string: ")
scrambletable = ' '.maketrans('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba')

scramble = myString.translate(scrambletable)
print(scramble)
