from collections import Counter

nums = [1,1,1,1,5,5,6,7]

freq1 = {}
for i in nums:
    if i in freq1:
        freq1[i] += 1
    else:
        freq1[i] = 1
        
        
freq2 = Counter(nums)

print(type(freq1))
print(type(freq2))


for i in freq1:
    print(i)