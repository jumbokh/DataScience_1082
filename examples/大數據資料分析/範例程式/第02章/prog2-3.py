import math
side = eval(input('Enter length of a side: '))
area = (5 * side ** 2) / (4 * math.tan(math.pi/5))
print('Area of 5-side is %.2f'%(area))