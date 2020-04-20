import random
again = 1
while again == 1:
    for i in range(1, 7):
        lotto = random.randint(1, 49)
        print('%3d'%(lotto), end = '')
    print()
    again = eval(input('Enter a number, 1 for continue, 0 for stop: '))