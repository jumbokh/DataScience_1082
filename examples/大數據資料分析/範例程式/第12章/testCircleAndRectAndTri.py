from circleFromShape import Circle
from rectangleFromShape import Rectangle
from triangleFromShape import Triangle

def main():
    circle = Circle(5)
    circle.__str__()
    print('Perimeter: %.2f'%(circle.getPerimeter()))
    print('Area: %.2f'%(circle.getArea()))
    print()    
    
    rectangle = Rectangle(2, 6)
    rectangle.__str__()
    print('Perimeter: %.2f'%(rectangle.getPerimeter()))
    print('Area: %.2f'%(rectangle.getArea()))
    print()

    triangle = Triangle(3, 0, 3, 4)
    triangle.__str__()
    print('Perimeter: %.2f'%(triangle.getPerimeter()))
    print('Area: %.2f'%(triangle.getArea()))

main()