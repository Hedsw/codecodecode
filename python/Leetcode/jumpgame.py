class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        ran = 0
        for num in nums:
            if i <= ran:
                ran = max(i + num, ran)
                # print(ran)
                i += 1
        return i >= len(nums)
    
# Greedy Algorithm 
# i <= reach, the furthest "start point" that I can reach
#   start point + nums[i] >= n, win!
#   start point + nums[i] < n, lose!
# so greedy
# Time Complexity is .. (M + N)