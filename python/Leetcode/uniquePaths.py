class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        
        for i in range(n):
            dp.append(1)
        #print(dp)
        
        dp = [dp] * m
        #print(dp, " h")
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]