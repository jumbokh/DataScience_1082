import random
lst = []
for i in range(1, 11):
    num = random.randint(1, 100)
    lst.append(num)
    
print('Original data:')
for x in lst:
    print('%3d'%(x), end = ' ')
print('\n')
    
# selection sort
for i in range(len(lst) - 1):
    min = lst[i]
    minIndex = i
    for j in range(i+1, len(lst)):
        if lst[j] < min:
            min = lst[j]
            minIndex = j

    if minIndex != i:
         lst[minIndex] = lst[i]
         lst[i] = min                  
#--------------------------------

print('Sorted data:')
for x in lst:
    print('%3d'%(x), end = ' ')