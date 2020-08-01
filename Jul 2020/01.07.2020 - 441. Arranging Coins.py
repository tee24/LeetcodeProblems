import math
def arrange_coins(n: int) -> int:
    return int((-1+math.sqrt(1+8*n))//2) # Solve inequality involving sum of natural numbers to arrive at this one liner.

# Space & Time: O(1)
