from circle import Circle
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