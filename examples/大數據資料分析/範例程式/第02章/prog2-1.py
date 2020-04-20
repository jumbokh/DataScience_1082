import math
radius = eval(input('Enter a radius: '))
area = math.pi * pow(radius, 2)
perimeter = 2 * math.pi * radius
print('radius of the circle is %d'%(radius))
print('area is %.2f, perimeter is %.2f'%(area, perimeter))