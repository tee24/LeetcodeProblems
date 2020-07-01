import math
def arrange_coins(n: int) -> int:
    return int((-1+math.sqrt(1+8*n))//2)

# Time: O(1)
# Space: O(1)
