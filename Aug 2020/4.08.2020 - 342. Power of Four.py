import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return math.log(num,4) == int(math.log(num,4)) if num > 0 else False


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num&(num-1) == 0 and 0b10101010101010101010101010101010101 & num == num
# Space, Time: O(1)

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
        	return False
        bin_num = bin(num)[2:]
        if bin_num.count('1') > 1:
        	return False
        return True if bin_num[::-1].index('1') % 2 == 0 else False


