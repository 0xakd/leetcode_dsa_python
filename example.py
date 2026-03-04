# Return the count of max duplicated number from a list = [1, 2, 3, 1, 2, 1, 3, 1, 0, 9]
def find_mode(nums: list[int]) -> int:
    mp = {}
    for i in nums:
        if i in mp:
            mp[i]+=1
        else:
            mp[i] = 1
    max_key = max(mp, key=mp.get)
    max_value = mp[max_key]
    return max_key, max_value

lst = [1, 2, 3, 1, 2, 1, 3, 1, 0, 9]
print(find_mode(lst))