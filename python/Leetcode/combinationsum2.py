class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        if len(candidates) == 0:
            return ans
        
        if target == 0:
            return ans
        
        candidates.sort()

        self.dfs(candidates, target, ans, [])
        return ans
    
    
    def dfs(self, candidates, target, ans, path):
        
        if target < 0:
            return 
        
        if target == 0:
            ans.append(path)
             
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
                
            if candidates[i] > target:
                break
                
            self.dfs(candidates[i+1:], target - candidates[i], ans, path + [candidates[i]])
        