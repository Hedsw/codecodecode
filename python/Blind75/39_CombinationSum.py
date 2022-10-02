# Time complexity - O(n^2) more detail.. O(N^(M/min_candidate + 1)), N = len(candidates), M = target, min_candidate = min(candidates)
# examined ~ binomial(n,1) + ... + binomial(n,n), so O(2^n),
# Space - O(target/min_candidate)
class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)
            