import random
# selection sort
def selectionSort(lst2):
    for i in range(len(lst2) - 1):
        min = lst2[i]
        minIndex = i
        for j in range(i+1, len(lst2)):
            if lst2[j] < min:
                min = lst2[j]
                minIndex = j

        if minIndex != i:
             lst2[minIndex] = lst2[i]
             lst2[i] = min
#--------------------------------

def main():
    lst = []
    for i in range(1, 11):
        num = random.randint(1, 100)
        lst.append(num)
    
    print('Original data:')
    for x in lst:
        print('%3d'%(x), end = ' ')
    print('\n')

    selectionSort(lst)
    print('Sorted data:')
    for x in lst:
        print('%3d'%(x), end = ' ')

main()