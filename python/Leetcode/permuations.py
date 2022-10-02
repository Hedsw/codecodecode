class Solution:
    #  time complexity of DFS if the entire tree is traversed is O(V) where V is the number of nodes. 
    # Deep Copying으로 내부 서치를 하기 때문에 Time Complexity는 O(n!)이다.. List로 딥카피 하니까
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 0:
            return
        
        self.dfs(nums, ans, [])
        
        return ans
    
    
    def dfs(self, nums, ans, path):
        
        if len(nums) == 0:
            ans.append(path)
            return
        
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], ans, path + [nums[i]])