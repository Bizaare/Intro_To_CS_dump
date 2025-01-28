# Author : Levi Yates
# Date   : 10-03-2022
# This program does fun things with circles & spheres...

# This is the start of the program

import circlesphere

r = float(input("Input the radius of a circle or sphere: "))
print("You entered " + str(r) + " as the radius.")

myDiameter = circlesphere.diameter(r)
print("The diameter = " + str(myDiameter) + " units.")

myCircumference = circlesphere.circumference(r)
print("The cirumference = " + str(myCircumference) + " units.")

myArea = circlesphere.area(r)
print("The area = " + str(myArea) + " square units.")

myBeachBallVolume = circlesphere.sphere_volume(r)
print("The volume of my beach ball is " + str(myBeachBallVolume) + "cubic units.")
print("I'll need " + str(circlesphere.sphere_surfacearea(r))
      + " square units of material to cover the beach ball.")

print("The volume of a dome house is "
     + format(circlesphere.hemisphere_volume(r), ',.2f') + " cubic units.")

print("The volume of Earth is: "
     + format(circlesphere.sphere_volume(3958.8), ',.0f') + " cubic miles.")

print("The surface area of a hemisphere is: "
     + str(circlesphere.hemisphere_surfacearea(r)) + " square units.")
