class Solution:
    def topKFrequent(self, nums, k):
        if not nums:
            return None
        count = {}

        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1

        ans = [[k,v] for k,v in list(count.items())[:k]]

        smallest = min(ans, key=lambda u:u[1])

        for k,v in count.items():
            if v > smallest[1] and [k,v] not in ans:
                ans.remove(smallest)
                ans.append([k,v])
                smallest = min(ans, key=x[1])

        return [i[0] for i in ans]

class Solution:
    def topKFrequent(self, nums, k):
        if not nums:
            return None
        count = {}
        bucket = [[] for _ in range(len(nums)+1)]
        for num in nums:
            count[num]=count.get(num,0)+1
        for key,val in count.items():
            bucket[val].append(key)
        ordered_freq = [i for x in bucket for i in x][::-1]
        return ordered_freq[:k]

#^^^^^^^^^ Space, Time: O(n) ^^^^^^^^^^^

import heapq
class Solution:
    def topKFrequent(self, nums, k):
        if not nums:
            return None
        count = {}
        for num in nums:
            count[num]=count.get(num,0)+1
        return heapq.nlargest(k, count.keys(), key=count.get)