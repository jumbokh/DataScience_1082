import random
def rand(n):
    for i in range(1, n+1):
        rn = random.randint(1, 100)
        if i % 10 == 0:
            print('%4d'%(rn))
        else:
            print('%4d'%(rn), end = ' ')

def main():
    num = eval(input('Enter num: '))
    rand(num)

main()