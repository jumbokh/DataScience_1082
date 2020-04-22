from circleFromShape import Circle
from rectangleFromShape import Rectangle

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
    print()

main()