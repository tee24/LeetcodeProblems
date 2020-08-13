class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        citations.sort()
        citations = citations[::-1]

        
        if citations[-1] >= len(citations):
            return len(citations)

        for i in range(1, len(citations)+1):
            if i > citations[i-1]:
                return i-1
        
        
    
# i = 1 : [6*,5,3,1,0] - 1 is not greater than 6 so continue...
# i = 2 : [6,5*,3,1,0] - 2 is not greater than 5 so continue...
# i = 3 : [6,5,3*,1,0] - 3 is not greater than 3 so continue...
# i = 4 : [6,5,3,1*,0] - 4 is greater than 1 so we know that there are 3 papers with at least 3 citations by above and 2 papers with at most 3 citations (since we know they have less than 4 by this line) hence h-index is 3.
