### Optimised approach ###
## Time Complexity :- O(n)
def twoSum(nums: list[int], target: int) -> list[int]:
    tempDict = {}
    for i in range (0, len(nums)):
        compliment = target - nums[i]
        if compliment in tempDict:
            return tempDict[compliment],i
        else:
            tempDict[nums[i]] = i
    return []

lst = [2,7,11,15]
t = 17

print(twoSum(lst, t))
