class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = [] 
        
        if len(digits) == 0:
            return res
        
        self.dfs(dic, digits, res, 0, '')
        return res
        
    def dfs(self, dic, digits, res, index, path):
        
        if len(digits) <= index:
            res.append(path)
            return
            
        _str = dic[digits[index]]
        
        for i in _str:
            self.dfs(dic, digits, res, index+1, path+i)
            