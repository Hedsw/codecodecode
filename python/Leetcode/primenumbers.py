class Solution:
    def countPrimes(self, n: int) -> int:
        
        lst = [True]*n
        
        if n < 3:
            return 0 
        lst[0], lst[1] = 0, 0
        m = 2 
        while m*m < n:
            if lst[m]:
                for i in range(m*m, n, m):
                    lst[i] = False
            
            m += 1
        
        return sum(lst)
            
        # Sieve of Eratosthenes를 사용해서 푸는 것 
        
        