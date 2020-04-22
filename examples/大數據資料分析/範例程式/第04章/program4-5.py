for i in range(1, 10):
    #add spaces
    for j in range(9, i, -1):
        print('  ', end = '')
    
    for k in range(1, i+1):
        print(i, end = ' ')
    print()