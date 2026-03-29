### Brute Force approach ###
## Time Complexity: O(n^2)


def containsDuplicate(nums: list[int]) -> bool:
    for i in range(0, len(nums)):
        for j in range (0, len(nums)):
            if i != j and nums[i] == nums[j]:
                return True
    return False

lst = [2,7,11, 2, 15]
t = 17

print(containsDuplicate(lst))
