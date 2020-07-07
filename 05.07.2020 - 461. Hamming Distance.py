class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x==y:
            return 0
        return bin(x^y).count('1')

#Time: O(n), Space O(1)