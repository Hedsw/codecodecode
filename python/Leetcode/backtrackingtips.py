class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 0:
            return
        
        nums.sort() # 이거도 duplication 제거할 때, 먼저 sort를 여기서 해줌
        self.dfs(nums, ans, [])
        
        return ans
    
    def dfs(self, nums, ans, path):
        
        if len(nums) == 0: # len(nums)해주는거는 num의 len과 같아야 할 경우에 이거 쓰면 됨 
            ans.append(path)
            return
        
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0: # 이거는 주로 Duplication 제거할 때 사용함 (Unique 한거 찾을 때)
                continue
            self.dfs(nums[:i] + nums[i+1:], ans, path + [nums[i]])