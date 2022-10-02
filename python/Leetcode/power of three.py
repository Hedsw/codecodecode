class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 2:
            if n % 3 != 0:
                return False
            
            n = n / 3
            
        return True if n == 1 else False