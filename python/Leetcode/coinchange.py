# Time Complexity is.. amount * coint number = M * N 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        rs = [amount+1] * (amount + 1)
        rs[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)
                
        if rs[amount] == amount + 1:
            return -1
        
        return rs[amount]
    
    """
내가 한거... 이거 틀린건데.. DP
    
    
    # Time Complexity is.. amount * coint number = M * N 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        
        #print(coins)
        counts = 0 
        i = 1
        if len(coins) == 1 and amount == 0:
            return 0
        
        if len(coins) == 1 and amount < coins[0]:
            return -1
        
        while coins[0] <= amount:
            if amount >= coins[len(coins) - i]:
                print(coins[len(coins) -i] , i)
                counts += 1
                amount = amount - coins[len(coins) - i]
                i = i - 1
            i = i + 1
            
        if amount != 0:
            return -1
        
        print(counts)
        return counts
    
        
        
    
        "