import os.path
def main():
    while True:
        try:
            filename = input('Enter a filename: ').strip()
            infile = open(filename, 'r')
            break
        except IOError:
            print('File: %s does not exist. Try again'%(filename))
            
    counts = 26 * [0]
    for line in infile:
        countLetters(line.lower(), counts)

    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + ' appears ' + str(counts[i])
                    + (' time' if counts[i] == 1 else ' times'))
    infile.close()

def countLetters(line, counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

main()