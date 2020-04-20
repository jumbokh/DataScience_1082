import random
def menu():
    print()
    print('Dictionary menu:')
    print('1. insert')
    print('2. delete')
    print('3. display')
    print('4. exit')
    n = eval(input('Enter your choice: '))
    return n

def add(d2):
    key = eval(input('Enter a key: '))
    value = input('Enter a value: ')
    print('generating ... {%d: \'%s\'}'%(key, value))
    d2[key] = value

def delete(d2):
    key = eval(input('Enter a key: '))
    if key in d2:
        print('{%d: \'%s\'} has been deleted'%(key, d2.get(key)))
        d2.pop(key)
    else:
        print('There is not invalid key.')

def display(d2):
    print(d2.items())

def main():
    d = {}
    while True:
        choice = menu()

        if choice == 1:
            add(d)
        elif choice == 2:
            delete(d)
        elif choice == 3:
            display(d)
        elif choice == 4:
            break
        else:
            print('Invalid choice')

main()