# Author : Levi Yates
# Date: 10-03-2022
# Module that does various computations for a circle/sphere

# circlesphere.py
"""Computations for a circle / sphere."""

import math

def diameter(radius):
    """Compute diameter of a circle
    given its radius."""
    diameter = radius * 2
    return diameter

def circumference(radius):
    """Compute circumference of a circle
    given its radius."""
    circ = 2 * math.pi * radius
    return circ

def area(radius):
    """Compute the area of a circle
    given its radius."""
##    a = math.pi * radius * radius
##    a = math.pi * radius **2
    a = math.pi * math.pow(radius, 2)
    return a

def sphere_volume(radius):
    """Compute the volume of a sphere
    given its radius."""
    volume = 4/3 * math.pi * radius**3
    return volume

def sphere_surfacearea(radius):
    """Compute the surface area of a sphere
    given its radius."""
    surfaceArea = 4 * math.pi * radius **2
    return surfaceArea

def hemisphere_volume(radius):
    """Compute the volume of a hemisphere
    given its radius."""
    #volume = 2/3 * math.pi * radius**3
    volume = sphere_volume(radius) / 2
    return volume

def hemisphere_surfacearea(radius):
    """Compute the surface area of a hemisphere
    given its radius."""
    surfaceArea = sphere_surfacearea(radius) / 2 + area(radius)
    return surfaceArea


    
