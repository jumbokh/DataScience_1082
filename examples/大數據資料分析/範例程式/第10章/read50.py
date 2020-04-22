import os.path
def main():
    infile = open('fruits.dat', 'r')
    if os.path.isfile('fruits.dat'):
        print('Using read(): ')
        print(infile.read())
    infile.close()

main()