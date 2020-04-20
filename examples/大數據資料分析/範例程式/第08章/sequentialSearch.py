import random
def randNum():
    randLst = []
    count = 1
    while count <= 6:
        num = random.randint(1,49)
        if num not in randLst:
            randLst.append(num)
            print('%3d'%(num), end = ' ')
            count += 1
    print()
    return randLst

def seqSearch(key, lst2):
    for i in range(len(lst2)):
        if key == lst2[i]:
            print('I got %d at lst2[%d]'%(key, i))
            return True

def main():
    lst = randNum()
    sn = eval(input('What number do you search? '))

    bool = seqSearch(sn, lst)
    if bool != True:
        print('%d is not found.'%(sn))

main()