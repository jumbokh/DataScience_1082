def main():
    s = input("Enter a binary number string: ").strip()
    v = binaryToDecimal(s)
    print("The decimal value is", v)

def binaryToDecimal(binaryString):
    value = ord(binaryString[0]) - ord('0')
    for i in range(1, len(binaryString)):
        value = value * 2 + ord(binaryString[i]) - ord('0')
    return value

main()