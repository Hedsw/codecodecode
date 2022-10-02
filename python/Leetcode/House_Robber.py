class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        newInt = [0]*len(nums)
        
        newInt[0] = nums[0]
        newInt[1] = max(nums[0], nums[1])
        
        
        for i in range(2, len(nums)):
            newInt[i] = max(nums[i] + newInt[i-2], newInt[i-1])
        
        return newInt[len(nums)-1]
    