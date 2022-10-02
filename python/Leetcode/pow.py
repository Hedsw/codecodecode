class Solution:
    def myPow1(self, x: float, n: int) -> float:
        return x ** n
    
    def myPow2(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow2(x, -n)
        if n % 2:
            return x * self.myPow2(x, n-1)
        return self.myPow2(x*x, n/2)