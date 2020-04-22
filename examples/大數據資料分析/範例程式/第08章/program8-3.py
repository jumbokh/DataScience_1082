import random   
# bubble sort
def bubbleSort(lst2):
    for i in range(len(lst2)-1):
        flag = 0
        for j in range(len(lst2)-i-1):
            if lst2[j] > lst2[j+1]:
                lst2[j], lst2[j+1] = lst2[j+1], lst2[j]
                flag = 1
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