class Solution:
    def prisonAfterNDays(self, cells, N):
        seen = {}
        for i in range(N):
            temp = [0]*8
            for j in range(1,7):
                temp[j] = int(cells[j-1] == cells[j+1]) # Update new configuration.
            if str(temp) in dict:
                return self.prisonAfterNDays(cells, (N-i)%(i - seen[str(temp)])) # If we have seen this configuration before then there must be cycle, call the function again mod the cycle length to skip remaining cycles.
            else:
                seen[str(temp)] = i # Used to determine length of cycle.
                cells = temp # Update cells configuration to be used on next iteration.       
        return cells

#Time and Space: O(1)





