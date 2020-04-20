import random
def lotto():
    for i in range(1, 7):
        n = random.randint(1, 49)
        print(n, end = ' ') 

def main():
    lotto()

main()