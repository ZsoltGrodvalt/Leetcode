# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(x):
    string = str(x)
    print(string)
    size = len(string)
    print(size)
    idx = 0
    while idx <= (size/2):
        if string[idx] != string[size-idx-1]:
            return 'false'
    return 'T=true'

x = 121
print(isPalindrome(x))

x = -121
print(isPalindrome(x))

x = 12111
print(isPalindrome(x))