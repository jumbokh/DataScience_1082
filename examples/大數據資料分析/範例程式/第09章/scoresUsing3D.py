scores3Dim = [
    [[80, 88, 90], [78, 76, 88], [90, 91, 90]],
    [[70, 68, 89], [88, 86, 82], [80, 86, 92]],
    [[77, 78, 83], [75, 78, 79], [89, 91, 90]],
    [[72, 87, 92], [74, 86, 88], [90, 94, 95]],
    [[82, 68, 90], [67, 66, 68], [70, 71, 82]]]

print('%13s %8s %8s'%('Calcu', 'Accou', 'Prog'))
print('%13s %8s %8s'%('-----', '-----', '----'))

for i in range(len(scores3Dim)):
    print('#%d: '%(i+1), end = '')
    for j in range(len(scores3Dim[i])):
        total = 0
        for k in range(len(scores3Dim[i][j])):
            total += scores3Dim[i][j][k]
        average = total / 3
        print('%9.2f'%(average), end = '')
    print()