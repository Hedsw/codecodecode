class Solution(object):
    def permute(self, nums):
        ans = []        
        
        if len(nums) == 0:
            return ans
        
        self.helper(nums, ans, [])
        return ans
    
    def helper(self, nums, ans, tmp):
        
        if len(nums) == 0:
            ans.append(tmp)
            
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], ans, path + [nums[i]])