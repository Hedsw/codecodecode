class Solution:
    def romanToInt(self, s: str) -> int:
        summary, prev = 0, 0
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        for i in s[::-1]:
            if dict[i] >= prev:
                summary += dict[i]
            else:
                summary -= dict[i]
            prev = dict[i]
        return summary