from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        add_one = False
        c = Counter(s)
        for letter, count in c.items():
            if count != 1:
                if count % 2 == 0:
                    length+=count
                else:
                    length+=(count-1)
                    add_one = True
            else:
                add_one = True
        return length+1 if add_one else length

#Space, Time = O(n) n = len(s)
