class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        count = 0
        for i in range(len(time)):
            for j in range(i+1, len(time)):
                _sum = time[i] + time[j]
                
                if _sum % 60 == 0:
                    print(time[i], time[j])
                    count = count + 1
        return count