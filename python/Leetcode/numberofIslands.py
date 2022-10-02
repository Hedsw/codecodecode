class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        if not grid:
            return 0 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.callDFS(grid, i, j)
                    count = count + 1
        return count
                           
    def callDFS(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0':
            return 
        
        grid[i][j] = '0'
        print(i,j)
        
        print(grid)
                           
        self.callDFS(grid, i+1, j)      
        self.callDFS(grid, i-1, j)      
        self.callDFS(grid, i, j+1)      
        self.callDFS(grid, i, j-1)      
        

                