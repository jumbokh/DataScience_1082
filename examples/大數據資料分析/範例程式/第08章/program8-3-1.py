import random   
def main():
    lst = []
    for i in range(1, 11):
        num = random.randint(1, 100)
        lst.append(num)
    
    print('Original data:')
    for x in lst:
        print('%3d'%(x), end = ' ')
    print('\n')

    lst.sort()
    print('Sorted data:')
    for x in lst:
        print('%3d'%(x), end = ' ')

main()
