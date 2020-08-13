class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""
        for char in s:
        	if char.isalpha():
        		clean_string+=char.lower()
        	elif char.isnumeric():
        		clean_string+=char
        left, right = 0, len(clean_string)-1

        while left < right:
        	if clean_string[left] != clean_string[right]:
        		return False
        	left+=1
        	right-=1

        return True
        