def main():
    f1 = input('Enter a source filename: ').strip()
    f2 = input('Enter a target filename: ').strip()

    # Open files for input 
    infile = open(f1, 'r')
    
    s = infile.read() # Read all from the file
    print('Original text is \'%s\''%(s))
    
    newString = ''
    
    for i in range(len(s)):
        newString += chr(ord(s[i]) + 2)
    print('After Encrypted text is \'%s\''%(newString))
    
    infile.close()  # Close the input file
    outfile = open(f2, 'w')   
    outfile.write(newString)
    outfile.close() # Close the output file

main()