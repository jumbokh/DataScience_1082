import math
class Shape:
    def __init__(self, xPoint = 0, yPoint = 0):
        self.__xPoint = xPoint
        self.__yPoint = yPoint

    def getPoint(self):
        return self.__xPoint, self.__yPoint

    def setPoint(self, xPoint, yPoint):
        self.__xPoint = xPoint
        self.__yPoint = yPoint

    def __str__(self):
        print('xPoint = %d, yPoint = %d'%(self.__xPoint, self.__yPoint))

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

class Rectangle(Shape):
    def __init__(self, width = 1, height = 1):
        super().__init__()
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        super().__str__()
        print('width: %d'%(self.__width))
        print('height: %d'%(self.__height))

def main():
    circle = Circle(5)
    circle.__str__()
    print('Perimeter: %.2f'%(circle.getPerimeter()))
    print('Area: %.2f'%(circle.getArea()))
    print()    
    
    rectangle= Rectangle(2, 6)
    rectangle.__str__()
    print('Perimeter: %.2f'%(rectangle.getPerimeter()))
    print('Area: %.2f'%(rectangle.getArea()))

main()