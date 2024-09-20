def isWordPalindrome(word):
    length = len(word)
    for i in range(0,length//2):
        l = word[i]
        r = word[length-1-i]
        if l != r:
            return False
    return True

def shortestPal(s):
    length = len(s)

    if isWordPalindrome(s) == True:
        return s
      
    for i in range(0,length):
        begin = s[:length-i]
        if isWordPalindrome(begin) == True:
            new = s[length-i:][::-1] + s
            return new

    

print(shortestPal('abbacd'))