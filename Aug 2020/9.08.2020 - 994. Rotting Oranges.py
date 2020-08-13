from typing import List
import copy

class Solution:
    def is_solvable(self, grid):
        def dfs(new_grid, i, j):
            if not(0<=i<=len(new_grid)-1) or not(0<=j<=len(new_grid[0])-1):
                return
            if new_grid[i][j] == 1:
                new_grid[i][j] = 2
            if new_grid[i][j] == 2:
                new_grid[i][j] = '*'
                dfs(new_grid, i-1, j)
                dfs(new_grid, i+1, j)
                dfs(new_grid, i, j+1)
                dfs(new_grid, i, j-1)
        
        new_grid = copy.deepcopy(grid)

        for i in range(len(new_grid)):
            for j in range(len(new_grid[0])):
                if new_grid[i][j] == 2:
                    dfs(new_grid,i,j)

        for i in range(len(new_grid)):
            for j in range(len(new_grid[0])):
                if new_grid[i][j] == 1:
                    return False

        return True

    def is_rotten(self, grid):
        for i in grid:
            for j in i:
                if j == 1:
                    return False
        return True

    def make_rotten(self, grid, i,j):
        if 0<=i<=len(grid)-1 and 0<=j<=len(grid[0])-1:
            if grid[i][j] == 1:
                grid[i][j] = 2

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if self.is_rotten(grid): # check if already everything is rotten
            return 0

        if not self.is_solvable(grid):
            return -1

        mins = 0

        while not self.is_rotten(grid):
            temp = []
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        temp.append([i,j])

            for i,j in temp:
                self.make_rotten(grid, i-1,j)
                self.make_rotten(grid, i+1,j)
                self.make_rotten(grid, i,j-1)
                self.make_rotten(grid, i,j+1)
            mins+=1

        return mins
