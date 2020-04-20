import random
def main():
    lottos = []
    outfile = open('lottoNumbers.dat', 'w')
    for i in range(6):
        num = random.randint(1, 49)
        if num not in lottos:
            lottos.append(num)
            outfile.write(str(num) + ' ')
    outfile.close()

    infile = open('lottoNumbers.dat', 'r')
    s = infile.read()
    lottoNums = [eval(x) for x in s.split()]
    for num in lottoNums:
        print(num, end = ' ')
    infile.close()

main()