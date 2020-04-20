def main():
    infile = open('fruits.dat', 'r')
    print('Using readlines(): ')
    print(infile.readlines())
    infile.close()

main()