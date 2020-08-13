class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]

        out = [[1],[1,1]]

        for i in range(2, rowIndex+1):
            temp = [1]
            for j in range(len(out[i-1])-1):
                temp.append(out[i-1][j]+out[i-1][j+1])
            temp.append(1)
            out.append(temp)

        return out[-1]

import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []

        for i in range(rowIndex+1):
            ans.append(math.factorial(k)//(math.factorial(i)*math.factorial(k-i)))

        return ans
