import random
def rand(a, b, n):
    for i in range(1, n+1):
        rn = random.randint(a, b)
        if i % 10 == 0:
            print('%4d'%(rn))
        else:
            print('%4d'%(rn), end = ' ')

def main():
    x, y, num = eval(input('Enter x, y, num: '))
    rand(x, y, num)

main()