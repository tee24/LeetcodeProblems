class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        a = 1
        b = 2

        for _ in range(3,n+1):
            a, b = b, a+b

        return b

# Space, Time: O(1), O(n)