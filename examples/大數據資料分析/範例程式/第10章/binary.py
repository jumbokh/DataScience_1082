import pickle
def main():
    outfile = open('binary.dat', 'wb')
    pickle.dump('John', outfile)
    pickle.dump(92, outfile)
    pickle.dump('Mary', outfile)
    pickle.dump(88, outfile)
    pickle.dump([10, 20, 30, 40, 50], outfile)
    outfile.close()

    infile = open('binary.dat', 'rb')
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))

    infile.close()

main()