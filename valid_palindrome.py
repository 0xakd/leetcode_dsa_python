import string

def isPalindrome(s: str):
    unwanted = string.punctuation + " "
    s = s.lower()
    
    for c in unwanted:
        s = s.replace(c, "")
    return s == s[-1::-1]

s = "A man, a plan, a canal: Panama"
isPalindrome(s)