class Solution:
    def singleNumber(self, nums):
    	seen = {}
    	ans = []
    	for num in nums:
    		if num in seen:
    			del seen[num]
    		else:
    			seen[num]=1
    	
    	return list(seen.keys())

# Space, Time: O(n)




