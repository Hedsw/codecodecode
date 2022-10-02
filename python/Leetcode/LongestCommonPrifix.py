class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sz, ret = zip(*strs), ""
        
        for i in sz:
            if len(set(i)) > 1:
                   break
            ret += i[0]
        return ret
        
        
        # zip(*strs) 의 뜻은 list안에 있는 str[0], str[1] ... 마지막에 있는 Element들까지 전부 다 zip안에 넣겠다는 뜻. 
        
        
        