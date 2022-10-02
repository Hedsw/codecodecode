class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]
        
        for i in range(2, n+1):
            steps.append(steps[i-1] + steps[i-2])
        return steps[n-1]
        