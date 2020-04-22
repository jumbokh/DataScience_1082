import random
def modify(lst2):
    for i in range(len(lst2)):
        if lst2[i] % 2 == 0:
            lst2[i] *= 2

def main():
    lst = []
    for i in range(1, 11):
        num = random.randint(1, 100)
        lst.append(num)
        
    print('Origianal list data:')
    for x in lst:
         print('%4d'%(x), end = ' ')
    print()

    #pass list to modify()
    modify(lst)
    
    print('After modified list:')
    for x in lst:
        print('%4d'%(x), end = ' ')

main()