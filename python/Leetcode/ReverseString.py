class Solution(object):
    # Space - O(N), Time - O(N) -> Split이 N이라서 
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        s = s.split()   
        left = 0
        right = len(s)-1
        while left < right:
            s[left] , s[right] = s[right],s[left] # Reverse Word by Word 
            left +=1
            right -=1
        return " ".join(s)

    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        """  
        s = " ".join(s.split())
        right = len(s)-1
        res = []
        tmp =''
        while right:
            if s[right] != ' ':
                tmp += s[right]
                right -=1
            else:
                res += tmp[::-1]+ ' '
                right -=1
                tmp =""
        res +=s[0]+tmp[::-1]
        tmp = ""
        return "".join(res)
