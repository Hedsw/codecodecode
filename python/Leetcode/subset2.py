class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        if len(nums) == 0:
            return ans
        
        self.dfs(nums, ans, [])
        
        return ans
        
        
    def dfs(self, nums, ans, path):
        
        ans.append(path)
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], ans, path + [nums[i]])
                