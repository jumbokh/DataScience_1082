from shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def __str__(self):
        super().__str__()
        print('radius: %d'%(self.__radius))