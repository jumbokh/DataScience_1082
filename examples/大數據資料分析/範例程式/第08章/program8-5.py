import random   
# bubble sort
def bubbleSort(lst2):
    for i in range(len(lst2)-1):
        flag = 0
        #print pass
        print('#%d pass: '%(i+1))
        for j in range(len(lst2)-i-1):
            if lst2[j] > lst2[j+1]:
                lst2[j], lst2[j+1] = lst2[j+1], lst2[j]
                flag = 1
            #print compare
            print('#%d compare: '%(j+1), end = '')
            for k in range(len(lst2)-i):
                print('%3d '%(lst2[k]), end = '')
            print()
        print()
        if flag == 0:
            break            
#----------------------------------

def main():
    lst = []
    for i in range(1, 11):
        num = random.randint(1, 100)
        lst.append(num)
    
    print('Original data:')
    for x in lst:
        print('%3d'%(x), end = ' ')
    print('\n')

    bubbleSort(lst)
    print('Sorted data:')
    for x in lst:
        print('%3d'%(x), end = ' ')

main()