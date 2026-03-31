def isAnagram(s: str, t: str) -> bool:
    # Convert both strings to lowercase and remove spaces
    s1, t1 = s.lower().replace(" ", ""), t.lower().replace(" ", "")

    # Create an array of size 26 to store counts of each character (a–z)
    arr = [0] * 26
    
    # Iterate through the first string and increase count of each character in the list
    for ch in s1:
        index = ord(ch) - ord('a')   # map character to index (0–25)
        arr[index] += 1
    
    # Iterate through the second string and decrease count
    for ch in t1:
        index = ord(ch) - ord('a')
        arr[index] -= 1
    
    # If both strings are anagrams, all values should be zero
    return arr == [0] * 26


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))