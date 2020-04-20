import random
def randNum(k):
    for i in range(1, k+1):
        n = random.randint(1, 100)
        print(n, end = ' ')        

def main():
    n = eval(input('How many random numbers do you want? '))
    randNum(n)

main()