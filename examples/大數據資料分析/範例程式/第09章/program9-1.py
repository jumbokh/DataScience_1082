lst44 = [
    [11,  2,  3, 14],
    [5,  16,  7,  8],
    [9,  10, 11, 12],
    [3,   2,  5,  1]]

smallest = 999999
indexOfCol = -1
for col in range(0, len(lst44[0])):
    total = 0
    for row in range(len(lst44)):
        total += lst44[row][col]
    print('Total of %d columns = %d'%(col, total))

    if total < smallest:
        smallest = total
        indexOfCol = col
    
print('The smallest value is %d, at column is %d'%(smallest, indexOfCol))