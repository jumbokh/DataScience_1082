import math
def nArea(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi/n))
    return area

def main():
    num = eval(input('Enter edge numebrs: '))
    side = eval(input('Enter side length: '))
    area2 = nArea(num, side)
    print('Area of %d edges is %.2f'%(num, area2))

main()