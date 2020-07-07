def island_perimeter(grid):
    def explore(grid,i,j):
        count = 0
        if (0<=i<len(grid)) and (0<=j<len(grid[0])):
            count+=int(not(grid[i][j]))
        else:
            count+=1
        return count

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter+=explore(grid,i-1,j)
                perimeter+=explore(grid,i+1,j)
                perimeter+=explore(grid,i,j-1)
                perimeter+=explore(grid,i,j+1)
    return perimeter

#Space:O(1), Time:O(nm) for n x m matrix.