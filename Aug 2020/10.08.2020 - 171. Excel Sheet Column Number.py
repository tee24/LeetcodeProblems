class Solution:
    def titleToNumber(self, s: str) -> int:
        answer = 0

        for i,j in enumerate(s):
            answer+=(26**(len(s)-i-1))*(ord(j)-64)

        return answer

#Space, Time: O(1), O(len(s))