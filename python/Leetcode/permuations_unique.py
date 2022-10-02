class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 0:
            return
        
        nums.sort()
        self.dfs(nums, ans, [])
        
        return ans
    
    
    def dfs(self, nums, ans, path):
        
        if len(nums) == 0:
            ans.append(path)
            return
        
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue
            self.dfs(nums[:i] + nums[i+1:], ans, path + [nums[i]])