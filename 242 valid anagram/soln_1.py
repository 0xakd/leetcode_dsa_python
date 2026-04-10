def isAnagram(s: str, t: str) -> bool:
    from collections import Counter
    return Counter(s) == Counter(t)

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))