class Solution:
    def isValid(self, s: str) -> bool:
        sLen = len(s)
        
        if sLen == 0:
            return False
        if sLen % 2 == 1:
            return False
        
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('[]','')
            s = s.replace('()', '')
            s = s.replace('{}','')
            sLen = len(s)
        
        return True if sLen == 0 else False
            
            
            
         