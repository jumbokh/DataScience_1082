def listAdd(lst11, lst22):
    lst33 = []
    for i in range(len(lst11)):
        lst33.append([])
        for j in range(len(lst22)):
            num = lst11[i][j] + lst22[i][j]
            lst33[i].append(num)
    return lst33

def displayList(lst):    
    for row in lst:
        for value in row:
            print('%5d'%(value), end = '')
        print()
            
def main():
    lst1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

    lst2 = [
        [2, 4, 6],
        [8, 10, 12],
        [14, 16, 18]]

    lst3 = listAdd(lst1, lst2)
    displayList(lst3)

main()