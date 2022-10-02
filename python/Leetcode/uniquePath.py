"""
One way to solve this problem is to use dynamic programming: define by dp[i][j] number of ways to reach point (i,j). How can we reach it, there are two options:
    We can reach it from above (i, j-1).
    We can reach it from the left: (i-1, j).
    That is all! We just evaluate dp[i][j] = dp[i-1][j] + dp[i][j-1]
Complexity: time comlexity is O(mn), space complexity is O(mn), which can be improved to O(min(m,n)).
"""
#1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
#2
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp = [[1] * n for _ in range(m)]
        dp = []
        for j in range(n):
            dp.append(1)         
        dp = [dp] * m
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

"""
2. Math solution
Note, that we need to make overall n + m - 2 steps, and exactly m - 1 of them need to be right moves and n - 1 down steps. By definition this is numbef of combinations to choose n - 1 elements from n + m - 2.

Complexity: time complexity is O(m+n), space complexity is O(1).
"""
class solution:
    def uniquePaths(self, m, n):
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp = [[1] * n for _ in range(m)]
        dp = []
        for j in range(n):
            dp.append(1)         
        dp = [dp] * m
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]