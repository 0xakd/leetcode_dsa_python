### Brute Force approach ###
## Time Complexity: O(n)


def containsDuplicate(nums: list[int]) -> bool:
    seen = {}
    for i in nums:
        if i in seen:
            return True
        else:
            seen[i] = True
    return False


lst = [2,7,11,2,15]
t = 17

print(containsDuplicate(lst))
