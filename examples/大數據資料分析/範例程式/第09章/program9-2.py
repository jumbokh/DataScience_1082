ans = [
       [1, 2, 3, 2, 2, 1, 4, 5, 2, 4],
       [2, 2, 4, 3, 4, 1, 4, 1, 3, 4],
       [1, 2, 3, 3, 3, 1, 2, 5, 2, 3],
       [1, 2, 3, 3, 2, 1, 3, 5, 2, 4],
       [1, 2, 3, 3, 2, 1, 5, 4, 2, 4],
       [3, 2, 2, 3, 2, 1, 4, 5, 1, 4]]

standAns =  [1, 2, 3, 3, 2, 1, 4, 5, 2, 4]

for i in range(len(ans)):
    correctNum = 0
    for j in range(len(ans[i])):
        if (ans[i][j] == standAns[j]):
            correctNum += 1
    print('#%d: %d'%(i+1, correctNum))