lst34 = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]]

for row in range(len(lst34)):
    total = 0
    for col in range(len(lst34[0])):
        total += lst34[row][col]
    print('Total of %d rows = %d'%(row, total))