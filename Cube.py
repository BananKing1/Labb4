"""
Same exercise as the previous one, but for a cube. The constructor should accept the length of a side as
parameter.
"""

import math

class cubes:
    def  __init__(self,side):
        self.side = side

    def getSide(self):
        return self.side

    def surfaceArea(self):
        return 6 * self.side**2

    def volume(self):
        return self.side**3

n = float(input("Input side: "))

cube1 = cubes(n)

print(cube1.getSide())
print(cube1.surfaceArea())
print(cube1.volume())
