def main():
    infile = open('fruits.dat', 'r')
    print('Using readline(): ')
    line1 = infile.readline()
    print(line1)
    print(repr(line1))
    infile.close()

main()