import random
num = random.randint(1, 1000)
if num % 3 == 0:
    print('%d is 3-multiple'%(num))
if num % 4 == 0:
    print('%d is 4-multiple'%(num))
if num % 7 == 0:
    print('%d is 7-multiple'%(num))
if (num % 3 !=0 and  num % 4 != 0 and num % 7 != 0):
    print('%d is not 3 or 4 or 7 multiple'%(num))