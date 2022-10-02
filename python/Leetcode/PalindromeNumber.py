class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if len(str(x)) == 1:
            return True
        if x > 0:
            Xstr = str(x)
            l = 0
            r = len(Xstr) - 1
            ans = True
            for i in range(len(Xstr)):
                if Xstr[i] != Xstr[r-i] and i < r - i:
                    print(i, r-i)
                    ans = False
            
            return ans