def main():
    try:
        number = eval(input('Enter a number: '))
        print('You enterde number is %d'%(number))
    except NameError as ex:
        print('Exception : %s'%(ex))

main()