import random
def lotto():
    for i in range(1, 7):
        n = random.randint(1, 49)
        print(n, end = ' ')
    print('\n')
    
def main():   
    again = 1
    while again == 1 :
        lotto()
        again = eval(input('Do you want to continue? 1 to continue, 0 to stop: '))
main()