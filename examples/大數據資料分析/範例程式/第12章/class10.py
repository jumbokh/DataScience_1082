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

def main():
    circle1 = Circle()
    print('circle1: radius is %d, perimeter is %.2f'%(circle1.radius, 
                         circle1.getPerimeter()))
    print('circle1: radius is %d, area is %.2f'%(circle1.radius, circle1.getArea()))

    print()
    circle2 = Circle(5)
    print('circle2: radius is %d, perimeter is %.2f'%(circle2.radius, 
                        circle2.getPerimeter()))
    print('circle2: radius is %d, area is %.2f'%(circle2.radius, circle2.getArea()))

    print('\nAfter set radius to 10')
    circle2.setRadius(10)
    print('circle2: radius is %d, perimeter is %.2f'%(circle2.radius, 
                       circle2.getPerimeter()))
    print('circle2: radius is %d, area is %.2f'%(circle2.radius, circle2.getArea()))

main()