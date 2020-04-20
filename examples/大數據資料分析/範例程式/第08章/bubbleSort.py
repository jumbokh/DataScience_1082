import random
lst = []
for i in range(1, 11):
    num = random.randint(1, 100)
    lst.append(num)
    
print('Original data:')
for x in lst:
    print('%3d'%(x), end = ' ')
print('\n')
    
# bubble sort
for i in range(len(lst)-1):
    flag = 0
    for j in range(len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            flag = 1
    if flag == 0:
        break            
#----------------------------------
                  
print('Sorted data:')
for x in lst:
    print('%3d'%(x), end = ' ')