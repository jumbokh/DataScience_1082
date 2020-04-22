import random
def randNum(k):
    for i in range(1, k+1):
        n = random.randint(1, 100)
        if i % 10 == 0:
            print('%3d'%(n))
        else:
            print('%3d'%(n), end = ' ')        

def main():
    n = eval(input('How many random numbers do you want? '))
    randNum(n)

main()