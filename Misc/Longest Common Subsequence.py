class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
	
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                grid[i][j] = 1 + grid[i-1][j-1] if text1[i-1] == text2[j-1] else max(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]
        