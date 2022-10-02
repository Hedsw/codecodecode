# Time Complexity is.. amount * coint number = M * N 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        rs = [amount+1] * (amount + 1)
        
        print(rs)
        
        rs[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)
                
        if rs[amount] == amount + 1:
            return -1
        
        return rs[amount]
    
        
        
    
        