class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        if len(nums) == 0:
            return res
        
        self.dfs(nums, res, [])
        return res
        
    def dfs(self, nums, res, path):
        
        res.append(path)
        
        for i in range(len(nums)):
            self.dfs(nums[i+1:], res, path + [nums[i]])
        
        
        