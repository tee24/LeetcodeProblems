from typing import List
# For each day we consider the two possibilites, either we have a stock or we do not.
# If we have a stock there are two options, either we bought that days stock or we carried a stock forward:
# Case 1: The stock was bought on that day, then the profit is dp[i-2][0]-prices[i] as we couldn't have sold yesterday. Case 2: Carry forward then it is dp[i-1][1]
# If we don't have a stock on day i then there are similarly two cases
# Case 1: Sell on that day: dp[i-1][1]+prices[i], or, Case 2: We simply carried forward: dp[i-1][0].
# Taking the max at each stage, finally return last element first value (it is better to finish without any stocks).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(prices[1]-prices[0], 0)

        dp = [[0,0] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], prices[1]-prices[0])
        dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])

        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i-1][1]+prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-2][0]-prices[i], dp[i-1][1])

        return dp[-1][0]

# Space, Time = O(n)

