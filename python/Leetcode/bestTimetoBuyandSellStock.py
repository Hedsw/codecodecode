# New Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = float('inf')
        maxValue = 0
        
        for i in prices:
            minValue = min(minValue, i)
            findValue = i - minValue
            maxValue = max(maxValue, findValue)
        return maxValue