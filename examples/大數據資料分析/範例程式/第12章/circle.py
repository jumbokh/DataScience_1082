import math
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getPerimeter(self):
        perimeter = 2 * self.radius * math.pi 
        return perimeter

    def getArea(self):
        area = self.radius * self.radius * math.pi
        return area