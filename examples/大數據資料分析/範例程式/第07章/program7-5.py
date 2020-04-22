def main():
    s = input('Enter a string for password: ').strip()
    if isValidPassword(s):
        print('Valid password')
    else:
        print('Invalid password')

# Check if a string is a valid password 
def isValidPassword(s):
    # Only letters and digits?
    if not s.isalnum():
        return False 

    # Check length
    if len(s) < 8:
        return False   

    # Count the number of digits
    count = 0
    for ch in s:
        if ch.isdigit(): 
            count += 1
    if count >= 3:
        return True
    else:
        return False

main()