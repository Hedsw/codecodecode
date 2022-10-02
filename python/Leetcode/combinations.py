class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        if n == 0 or k == 0:
            return ans
        
        self.dfs(range(1,n+1), k, [], ans)
        return ans
    
        
    def dfs(self, nums, index, path, ans):
        if len(path) == index:
            ans.append(path)
            return
        
        for i in range(len(nums)):
            self.dfs(nums[i+1:], index, path + [nums[i]], ans)