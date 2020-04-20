def isPalindrome(s):
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] != s[high]:
            return False
        low = low + 1
        high = high -1
    return True

def main():
    s = input('Enter a string: ')

    if isPalindrome(s):
        print('%s is a palindrome'%(s))
    else:
        print('%s is not a palindrome'%(s))

main()