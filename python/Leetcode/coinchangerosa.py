"""
It's actually a complete backpack problem:

capacity of the "backpack" is amount
coins represents value of each item you can put into the "backpack"
you can take 0 or many coins
for each coin the cost is constant 1
so the question is to find minimum cost to fill the "backpack"
"""

class Solution(object):
    def coinChange(coins, amount):
        dp = [0] + [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]
        

coins = [1,3,5,8,15,17,23]
amount = 19431

print(Solution.coinChange(coins, amount))