def main():
    try:
        n1, n2 = eval(input('Enter two numbers, separated by a comma: '))
        ans = n1 / n2
        print('%d/%d = %.2f'%(n1, n2, ans))
    except ZeroDivisionError:
        print('denominator can\'t be zero')
    except SyntaxError:
        print('A comma may be missing in the input')
    except:
        print('Something wrong in the input')
    else:
        print('No exception')
    finally:
        print('The finally clause is executed')

main()