import os.path
def main():
    outfile = open('fruits.dat', 'a')
    if os.path.isfile('fruits.dat'):
        outfile.write('Kiwi\n')
    outfile.close()

    infile = open('fruits.dat', 'r')
    if os.path.isfile('fruits.dat'):
        print(infile.read())
    infile.close()

main()