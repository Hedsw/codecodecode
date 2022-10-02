class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        row = len(grid)
        col = len(grid[0])
        
        # rotten check 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
        
        # rotten adjacent check
        def rootenadjcheck(rotten):
            temp = []
            
            for i,j in rotten:
                if i > 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    temp.append((i-1, j))
                if j > 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    temp.append((i, j-1))
                if i < row - 1 and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    temp.append((i+1,j))
                if j < col - 1 and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    temp.append((i, j+1))
            return temp
        
        # count value 
        count = 0
        while(1):
            rotten = rootenadjcheck(rotten)
            if len(rotten) == 0:
                break
            count += 1
        
        # check no adjacent orange is exist
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return count
                
                