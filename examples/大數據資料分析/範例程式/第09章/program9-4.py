def isMarkovMatrix(m):
    # Check positive
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] < 0:
                return False

        # Check the sum of each column
        for j in range(len(m[0])):
            sum = 0
            for i in range(len(m)):
                sum += m[i][j]
      
            if sum != 1:
                return False

    return True

def main():
    SIZE = 3
    print("Enter a 3 by 3 matrix row by row: ")
    m = []
    
    for i in range(SIZE):
        line = input().split()
        m.append([eval(x) for x in line])

    if isMarkovMatrix(m):
        print("It is a Markov matrix")
    else:
        print("It is not a Markov matrix")

main()