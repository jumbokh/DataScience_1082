import random
def randNum():
    randLst = []
    count = 1
    while count <= 6:
        num = random.randint(1,49)
        if num not in randLst:
            randLst.append(num)
            count += 1
    print()
    randLst.sort()
    return randLst

def binSearch(key, lst2):
    low = 0
    high = len(lst2) - 1
    count = 1
    while high >= low:
        mid = (low + high) // 2
        if key < lst2[mid]:
            high = mid - 1
        elif key == lst2[mid]:
            return mid, count
        else:
            low = mid + 1
        count += 1
    return -999, 99999

def main():
    lst = randNum()
    for x in lst:
        print('%3d'%(x), end = ' ')
    print()

    key = eval(input('What number do you search? '))
    n, c = binSearch(key, lst)    
    if n == -999:
        print('%d is not found.'%(key))
    else:
        print('I got %d at lst2[%d]'%(key, n))
        print('Numbers of compare: %d'%(c))

main()