import math
class Circle:
    def __init__(self, radius = 1):
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        perimeter = 2 * self.__radius * math.pi 
        return perimeter

    def getArea(self):
        area = self.__radius * self.__radius * math.pi
        return area

def main():
    circle1 = Circle()
    print('circle1: radius is %d, perimeter is %.2f'%(circle1.getRadius(), circle1.getPerimeter()))
    print('circle1: radius is %d, area is %.2f'%(circle1.getRadius(), circle1.getArea()))

    print()
    circle2 = Circle(5)
    print('circle2: radius is %d, perimeter is %.2f'%(circle2.getRadius(), circle2.getPerimeter()))
    print('circle2: radius is %d, area is %.2f'%(circle2.getRadius(), circle2.getArea()))

    print('\nAfter set radius to 10')
    circle2.setRadius(10)
    print('circle2: radius is %d, perimeter is %.2f'%(circle2.getRadius(), circle2.getPerimeter()))
    print('circle2: radius is %d, area is %.2f'%(circle2.getRadius(), circle2.getArea()))
    
main()