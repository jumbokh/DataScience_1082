from circleFromShape import Circle
from rectangleFromShape import Rectangle

def main():
    circle = Circle(5)
    rectangle= Rectangle(2, 6)

    print('Circle information')
    displayInform(circle)
    print()
    
    print('Rectangle information')
    displayInform(rectangle)
    print()

def displayInform(obj):
    print('Area: %.2f'%(obj.getArea()))
    print('Permiter: %.2f'%(obj.getPerimeter()))  
    if isinstance(obj, Circle):
        print('Radius: %d'%(obj.getRadius()))
    elif isinstance(obj, Rectangle):
        print('Width: %d'%(obj.getWidth()))
        print('Width: %d'%(obj.getHeight()))
        
main()