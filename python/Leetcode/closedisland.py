# Time Complexity for DFS O( V + E ) where V is the number of nodes, E is the number of edges.
# Total time complexity  => loop -> M*N + V+E 
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid) -1):
            for j in range(len(grid[0]) - 1): 
                if grid[i][j] == 0 and self.dfs(i, j, grid):
                    count = count + 1
        return count

    def dfs(self, i , j, grid):
        if grid[i][j] == 1:
            return True
        
        if i<=0 or j<=0 or i>=len(grid)-1 or j >=len(grid[0])-1:
            return
        
        grid[i][j] = 1
        
        down = self.dfs(i - 1, j, grid)
        up = self.dfs(i + 1, j, grid)
        left = self.dfs(i, j - 1, grid)
        right = self.dfs(i, j + 1, grid)
        #여기서 down, up, left, right가 다 True로 나오면... True
        
        return up and down and left and right