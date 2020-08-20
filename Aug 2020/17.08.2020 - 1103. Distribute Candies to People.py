from typing import List
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0 for _ in range(num_people)]
        person = 0
        candies_to_give = 1
        while candies > 0:
        	person%=num_people
        	ans[person]+=min(candies_to_give, candies)
        	candies-=min(candies_to_give, candies)
        	person+=1
        	candies_to_give+=1
        return ans
