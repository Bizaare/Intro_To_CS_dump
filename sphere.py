# Author : Levi Yates
# Date   : 2022-08-29
# This program calculates the volume and surface area of a sphere.

pi = 3.14159265

radius = int(input("What is the radius of your sphere? "))
surfaceArea = 4 * pi * radius ** 2
volume = 4 / 3 * pi * radius ** 3

print("Your sphere's Volume is: " + str(volume))
print("Your sphere's Surface Area is: " + str(surfaceArea))

print()
print("Clean-up")
print()

print("Your sphere's Volume is: " + format(volume, '2,.2f'))
print("Your sphere's Surface Area is: " + format(surfaceArea, '2,.2f'))


# End of program 
