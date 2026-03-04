

### Find the second largest number from the list of numbers - [-1, -2, -3, -1]

# def findSecondLargestElement(arr):
#     max = arr[0]
#     max2 = arr[0]
    
#     for i in arr:
#         if i > max:
#             max2 = max
#             max = i
#         elif i > max2 and i != max:
#                 max2 = i

#     print("Second largest element is: ", max2)
    
    
# arr = [1, 2, 5, 4] #[-1, -2, -3, -1] #[1, 2, 5, 4]
# findSecondLargestElement(arr)




### Find the smallest number in the sorted rotated array - [4, 5, 6, 0, 1, 2, 3]

# def func2(arr):
#     # temp = arr[0]
#     for i in range (0, len(arr)):
#         if arr[i]<arr[i+1]:
#             return i
    
# arr = [4, 5, 6, 0, 1, 2, 3]
# print("Smallest element: ",func2(arr))







### Find the numbers that sum to a target from the list - [4, 7, 2, 1, 0, -2, -5] t = -7

def findSubArraySum (arr, t):
    map = {}
    for i in range (0, len(arr)):
        compliment = t - arr[i]
        if compliment in map:
            return map[compliment], i
        else:
            map[arr[i]] = i
    return []    
    
arr = [4, 7, 2, 1, 0, -2, -5]
t = -7
print(findSubArraySum(arr, t))




### Find the valid pairs of anagrams from the list of words - ["eat", "cat", "bat", "ate", "tab"] => [["eat", "ate"], ["bat", "tab"]]
# def getAnagrams (lst):
#     for i in lst:
#         for j in lst:
#             if j == i:
#                 continue
#             if len[i] == len[j]:
#                 if 