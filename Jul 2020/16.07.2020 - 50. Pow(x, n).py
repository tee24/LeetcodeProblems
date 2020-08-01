class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            y = helper(x,n//2)
            
            if n%2==1:
                return y*y*x
            return y*y
        ans = helper(x,abs(n))
        
        return ans if n > 0 else 1/ans

# Space, Time: O(log(n))