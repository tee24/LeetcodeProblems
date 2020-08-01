class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        
        if word[0].islower():
            return False
        
        for i in word[1:]:
            if i.isupper():
                return False
        return True
# Space, Time: O(n) worst case.