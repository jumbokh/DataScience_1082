import random
def menu():
    print()
    print('Set menu:')
    print('1. insert')
    print('2. delete')
    print('3. display')
    print('4. exit')
    n = eval(input('Enter your choice: '))
    return n

def add(s2):
    x = random.randint(1, 49)
    print('generating ... %d'%(x))
    s2.add(x)

def delete(s2):
    x = eval(input('Enter a number: '))
    if x in s2:
        s2.remove(x)
    else:
        print('There is not invalid number.')

def display(s2):
    print(s2)

def main():
    s = set()
    while True:
        choice = menu()

        if choice == 1:
            add(s)
        elif choice == 2:
            delete(s)
        elif choice == 3:
            display(s)
        elif choice == 4:
            break
        else:
            print('Invalid choice')

main()