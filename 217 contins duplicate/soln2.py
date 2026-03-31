### Brute Force approach ###
## Time Complexity: O(log n)


def containsDuplicate(nums: list[int]) -> bool:
    lst = []
    for i in nums:
        if i in lst:
            return True
        else:
            lst.append(i)
    return False



lst = [2,7,11,15]
t = 17

print(containsDuplicate(lst))
