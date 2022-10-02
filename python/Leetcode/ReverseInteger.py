class Solution:
    def reverse(self, x: int) -> int:
        flag = False 
        if x < 0: # False mean Minus and True mean Plus
            flag = True
        
        if flag:
            x *= -1
        strInt = str(x)[::-1]
        always = int(strInt)
        
        if always > 2**31-1:
            return 0
        
        if flag:
            return always*(-1)
        else:
            return always