# Author : Levi Yates
# Date   : 2022-09-26
# this program is a lot of function examples
## [[-IMPORTS
import math


## -]]
# Accept two numbers and return the biggest of the two numbers.
# If the two numbers are exactly equal, then it returns the number.
def bigNumber(arg1, arg2):
    """Return the biggest of two numbers.
    For example bugNumber(23.7, 43.8) will
    return 43.8"""
    if arg1 > arg2:
        return arg1
    else:
        return arg2


# Enter a first name, middle, and last name.
#Function returns initials.
def makeInitials(fn, mn, ln):
    """Return initials of a name.
    For example, makeInitials("John", "Quincy", "Joe")
    will return JQJ"""
    initials = (fn[:1] + mn[:1] + ln[:1]).upper()
    return initials


# Program execution actually starts here after all functions.

# The goal of this program is to ask the user for two numbers.
# Print the larger number.
number1 = float(input("Enter the first number  : "))
number2 = float(input("Enter the second number : "))

print("Your numbers are as follows - Number 1 = " + str(number1) + "  & Number 2 = " + str(number2))


biggest = bigNumber(number1, number2)
print("The biggest of the two numbers is: " + str(biggest))

print()
biggest = bigNumber(56.3, 23.9)
print("This biggest of the two numbers is: " + str(biggest))

print()
print("The biggest of the  two numbers is: " + str(bigNumber(89.4, 45.2)))


print()
myAge = int(input("How old are you? "))
friendAge = int(input("How old is your friend? "))
print()
print("The oldest person is " + str(bigNumber(myAge, friendAge))
        + " years old.")
print()

# Enter a first name, middle name, and last name.
# Let's ask the user for their full name.
firstName = input("What is your first name  ? ")
middleName = input("What is your middle name ? ")
lastName = input("What is your last name   ? ")

initials = makeInitials(firstName, middleName, lastName)

print("Your initials are: " + initials)
print()
print(makeInitials("Susan", "ulga", "Savanna"))

# Do NOT do this. This will have unintended results.
# print = "The bigger number is : " + str(bigNumber(number1, number2))

print("Hello there.")
print()
print("Pi is " + str(math.pi))
# Do NOT even do this.
#math.pi = 7645646567825376852782357893124916354789623175862375862378537567488545678010918276546537 # I AM PI
print("Pi is actually " + str(math.pi) + " now.")
