# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(x):
    string = str(x)
    size = len(string)
    idx = 0
    while idx < (size/2):
        if string[idx] != string[size-idx-1]:
            return False
        idx += 1
    return True

x = 121
print(isPalindrome(x))

x = -121
print(isPalindrome(x))

x = 12111
print(isPalindrome(x))

x = 11
print(isPalindrome(x))