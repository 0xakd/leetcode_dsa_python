def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # returns false if the list is empty 
    if not strs:
        return []
    
    mpp = {} # an empty map

# returns a frequency string for each words
    def getFrequencyString(s: str):
        freq_list = [0] * 26

        for char in s:
            freq_list[ord(char) - ord('a')] += 1   # get the index value of characters and add +1 to it 

        freq_Str = []
        ch = 'a'

        for position in freq_list:
            freq_Str.append(ch)
            freq_Str.append(str(position))
            ch = chr(ord(ch)+1)

        return "".join(freq_Str)



    for i in strs:
        fStr = getFrequencyString(i)

        if fStr not in mpp:
            mpp[fStr] = []

        mpp[fStr].append(i)

    return list(mpp.values())