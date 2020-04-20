from circleFromShape import Circle
from rectangleFromShape import Rectangle

def main():
    circle = Circle(5)
    circle.__str__()
    displayPerimeter(circle)
    displayArea(circle)
    print()

    rectangle= Rectangle(2, 6)
    rectangle.__str__()
    displayPerimeter(rectangle)
    displayArea(rectangle) 
    print()   

def displayArea(obj):
    print('Area: %.2f'%(obj.getArea()))

def displayPerimeter(obj):
    print('Permiter: %.2f'%(obj.getPerimeter()))  
    
main()