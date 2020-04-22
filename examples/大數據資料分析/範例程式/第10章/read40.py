def main():
    infile = open('fruits.dat', 'r')
    print('Using readline(): ')
    line = infile.readline()
    while line != '':
        print(repr(line))
        line = infile.readline()
    infile.close()

    print()
    infile = open('fruits.dat', 'r')
    for line in infile:
        print(repr(line))
    infile.close()

main()