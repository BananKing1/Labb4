"""
Write a class to represent spheres. Your class should implement the following methods:
• __init__(self,radius) Creates a sphere having the given radius
• getRadius(self) Returns the radius of this sphere
• surfaceArea(self) Returns the surface aera of the sphere
• volume(self) Returns the volume of the sphere
Once the class has been writing, use it to write a program which takes as input the radius and prints
the corresponding surface aera and volume of the sphere
"""

import math

class spheres:
    def  __init__(self,radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return (4 * math.pi * self.radius**3)/3

n = float(input("Input radius: "))

sphere1 = spheres(n)

print(sphere1.getRadius())
print(sphere1.surfaceArea())
print(sphere1.volume())
