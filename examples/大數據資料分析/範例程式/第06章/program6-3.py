import random
def lotto(n):
    for i in range(1, n+1):
        for i in range(1, 7):
            lottoNum = random.randint(1, 49)
            print('%3d'%(lottoNum), end = ' ')
        print()

def main():
    num = eval(input('How many sets: '))
    lotto(num)

main()