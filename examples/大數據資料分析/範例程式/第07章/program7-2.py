def main():
    number = input("Enter the first 9 digits of an ISBN-10 number as a string: ").strip()
    # Calculate checksum
    sum = 0
    for i in range(9):
        sum += int(number[i]) * (i + 1)


    checksum = sum % 11
    print("The ISBN number is ", end = "")
    print(number, end = "")
    if checksum == 10:
        print("X")
    else:
        print(checksum)

main()