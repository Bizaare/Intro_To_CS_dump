# Author  : Levi Yates
# Date    : 2022-08-29
# Lecture notes from class

print("Hello world!")
print("This is line2")

print("I love programming.")

print("I can't go to bed.")

print('A famous quote "I dont have any good quotes" - Me right now')

print('This is a quote: "This text shouldn\'t work." - Me')

print("This is a quote: \"This test shouldn't work.\" - Me")

print()
print("C:\\Windows\\Users\\xxthe\\Documents\\")

total = 6 + 9.72

print(total)
print("My total =" + str(total))


Jager = "Katzen" #hunter
Opfer = "Mause"  #hunted 

print("Die " + Jager +" hat " + Opfer + " essen.")

Jager = "fox"
Opfer = "turkey"

print("Die " + Jager +" hat " + Opfer + " essen.")

print()
# Collection of personal information
print("Let's collect some information on you.")

firstName = input("What is your first name? ")
middleName = input("What is your Middle Name? ")
lastName = input("What is your last name? ")

fullName = str(firstName) + " " + str(middleName) + " " + str(lastName)
print("Your Name is: " + fullName)

print()
age = input("What is your age?")
print("You are " + age + " years old.")

print()
print("You are " + fullName + " and you are " + age + " years old.")

print()

height = int(input("How tall are you in inches? "))
print("You are " + str(height) + " inches tall")

heightFeet = height // 12
print("feet = " + str(heightFeet))

heightInches = height - heightFeet * 12
print("inches = " + str(heightInches))
print("Your height is " + str(heightFeet) + "'" + str(heightInches) + '" ')

# () paranthesis
# [] square brackets
# {} curly braces
# <> angle brackets

initials = (firstName[:1] + middleName[:1] + lastName[:1]).upper()
print("Your initials are " + initials)

print("Your name backwards is " + fullName[::-1])

# End of Program.
