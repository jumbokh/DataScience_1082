def main():
    s = input('Enter a string for SSN: ') .strip() 
    if isValidSSN(s): 
        print('Valid SSN')
    else:
        print('Invalid SSN')    

# Check if a string is a valid SSN 
def isValidSSN(ssn):
    return len(ssn) == 11 and ssn[0].isdigit() and \
      ssn[1].isdigit() and ssn[2].isdigit() and \
      ssn[3] == '-' and ssn[4].isdigit() and \
      ssn[5].isdigit() and ssn[6] == '-' and \
      ssn[7].isdigit() and ssn[8].isdigit() and \
      ssn[9].isdigit() and ssn[10].isdigit()

main()