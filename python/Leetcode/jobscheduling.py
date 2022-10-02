import functools
class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        if d > len(A):
            return -1
        n = len(A)
        @functools.lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(A[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, A[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res
        return dfs(0, d)
"""
dfs help find the the minimum difficulty
if start work at ith job with d days left.

If d = 1, only one day left, we have to do all jobs,
return the maximum difficulty of josbs.

"""
    
# Time complexity O(nnd)
# Space complexity O(nd)