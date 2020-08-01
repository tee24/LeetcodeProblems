def subsets(nums):
    output = [[]]
    print(output)
    for i in nums:
        output+=[subset+[i] for subset in output]
    return output
# Space, Time: O(N*2^N)

def subsets(nums):
    powerset = []
    for i in range((2**len(nums))):
        subset_repr = bin(i)[2:].zfill(len(nums))
        subset = []
        for index, value in enumerate(subset_repr):
            if value == '1':
                subset.append(nums[index])
        powerset.append(subset)
    return powerset 

class Solution:
    def subsets(self, nums):
        
        def backtrack(first=0, curr=[]):
            if len(curr) == length:
                output.append(curr[:])

            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        output = []
        n = len(nums)

        for length in range(n+1):
            backtrack()
        return output
        
from itertools import combinations

def powerset(s):
    for i in range(0, len(s)+1):
        for combination in combinations(s,i):
            yield combination

x = powerset([1,2,3])
print(list(x))


