from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    
    # creates a list of empty lists. for eg.- [[], [], [], []]
    bucket = [[] for _ in range(len(nums)+1)]
    
    # fill frequency_map with numbers and the number of times they appear in the list.
    frequency_map = Counter(nums)

    # fill bucket
    for key, freq in frequency_map.items():
        bucket[freq].append(key)
    
    result = []
    
    # iterate bucket in reverse to get top k elements
    for i in reversed(range(len(bucket))):
        if bucket[i]:
            for value in bucket[i]:
                if len(result)<k:
                    result.append(value)
                else:
                    return result
    return result

elements = [1,2,1,2,1,2,3,1,3,2]
output = (topKFrequent(elements, 2))
print(output)