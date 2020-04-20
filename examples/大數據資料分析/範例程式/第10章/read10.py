def main():
    infile = open('fruits.dat', 'r')
    print('Using read(): ')
    print(infile.read())
    infile.close()

    infile = open('fruits.dat', 'r')
    print('Using read(number): ')
    data = infile.read(12)
    print(data)
    print(repr(data))
    infile.close()

main()