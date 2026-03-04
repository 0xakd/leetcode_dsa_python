### Optimised approach ###
## Time Complexity :- O(n)
def twoSum(self, nums: list[int], target: int) -> list[int]:
    tempDict = {}
    for i in nums:
        compliment = target - nums[i]
        if compliment in tempDict:
            return tempDict[compliment],i
        else:
            tempDict[nums[i]] = i
    return [] 