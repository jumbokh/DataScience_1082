import math
def circle():
    radius = eval(input('Enter a radius: '))
    if radius <= 0:
        raise RuntimeError('Negative radius')
    else:
        area = radius * radius * math.pi
        perimeter = 2 * math.pi * radius
        print('Perimeter: %.2f, area: %.2f'%(perimeter, area))

def main():
    try:
        circle()
    except RuntimeError:
        print('Invalid radius')
        
main()