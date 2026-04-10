def isAnagram(s: str, t: str) -> bool:
    # Convert both strings to lowercase and remove spaces
    s1, t1 = s.lower().replace(" ", ""), t.lower().replace(" ", "")

    arr = [0]*26    # Create a list of size 26 to store frequency of each letter (a–z)
    
    # Increase count for each character in string s
    for i in s:
        arr[ord(i) - ord('a')] += 1    # Map character to index (0–25) and increment its count
    
    # Decrease count for each character in string t
    for i in t:
        arr[ord(i) - ord('a')] -= 1    # Map character to index (0–25) and decrement its count
        
    # If both strings are anagrams, all counts will be zero
    return arr == [0]*26

    
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))