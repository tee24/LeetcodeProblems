#Trivial Solution
def sum_digits(num):
    while len(str(num)) != 1:
        temp = 0
        for i in str(num):
            temp+=int(i)
        num = temp
    return num

#Mathmatical Solution: Space, Time: O(1)
def sum_digits(num):
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9


