### Brute Force approach###
## Time Complexity :- O(n^2)

def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range (0, len(nums)):
        for j in range (0, len(nums)):
            if (i != j and nums[i]+ nums[j] == target):
                return i, j
    return []
        
        
