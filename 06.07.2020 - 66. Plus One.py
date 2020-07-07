class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return None
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i]+=1
                break
            digits[i] = 0
            if i == 0:
                digits[i]=1
                digits.append(0)
        return digits
    
     def plusOne(self, digits: List[int]) -> List[int]:
        ans = int(''.join([str(x) for x in digits]))
        ans+=1
        ans = str(ans)
        ans = list(ans)
        return ans
    
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 1
        for i,j in enumerate(digits[::-1]):
            ans+=10**int(i)*j
        return list(str(ans))