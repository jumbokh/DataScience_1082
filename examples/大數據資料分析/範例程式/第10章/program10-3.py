def main():
    # Prompt the user to enter filenames
    f1 = input('Enter a filename: ').strip()

    # Open files for input 
    infile = open(f1, 'r')
    
    s = infile.read() # Read all from the file
    print(s)
    
    deletedString = input('Enter a string to be deleted: ').strip()
    
    newString = s.replace(deletedString, '')
    print(newString)
        
    infile.close()  # Close the input file
    outfile = open(f1, 'w')

    outfile.write(newString)
    outfile.close() # Close the output file

main()