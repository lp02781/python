import math
class Polygon():
    def __init__ (self, side=4, length=2):
        self.side=side
        self.length=length
    def area (self):
        return ((self.length**2)*self.side)/(4*math.tan(math.pi/self.side))
    def perimeter(self):
        return self.side*self.length
tobi = Polygon(3,2)
print(tobi.area())
print(tobi.perimeter())
