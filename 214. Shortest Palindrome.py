def isWordPalindrome(word):
            if word == word[::-1]:
                return True
            else:
                return False

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