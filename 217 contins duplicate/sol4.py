### Brute Force approach ###
## Time Complexity: O(log n)


def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))



lst = [2,7,11,15]
t = 17

print(containsDuplicate(lst))