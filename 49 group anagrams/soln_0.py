# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     # returns false if the list is empty 
#     if not strs:
#         return []
    
#     mpp = {} # an empty map

# # returns a frequency string for each words
#     def getFrequencyString(s: str):
#         freq_list = [0] * 26

#         for char in s:
#             freq_list[ord(char) - ord('a')] += 1   # get the index value of characters and add +1 to it 

#         freq_Str = []
#         ch = 'a'

#         for position in freq_list:
#             freq_Str.append(ch)
#             freq_Str.append(str(position))
#             ch = chr(ord(ch)+1)

#         return "".join(freq_Str)



#     for i in strs:
#         fStr = getFrequencyString(i)

#         if fStr not in mpp:
#             mpp[fStr] = []

#         mpp[fStr].append(i)

#     return list(mpp.values())




def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if not strs:
        return []
    
    mpp = {}
    
    def getFrequencyString(s: str):
        freqList = [0]*26
        
        for i in s:
            freqList[ord(i) - ord('a')] += 1
        
        
        freqStr = [] 
        ch = 'a'           
        for pos in freqList:
            freqStr.append(ch)
            freqStr.append(str(pos))
            ch = chr(ord(ch)+1)
            
        return "".join(freqStr)
    
    for i in strs:
        frequency_string  = getFrequencyString(i)
        
        if frequency_string not in mpp:
            mpp[frequency_string] = []
        
        mpp[frequency_string].append(i)
        
    return list(mpp.values())



lst = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']        
print("Group anagrams:")
print(groupAnagrams(lst))