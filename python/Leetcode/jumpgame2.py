class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1 and nums[0] == 0:
            return True
        sp = 0
        reach = 0
        for num in nums:
            if sp <= reach:
                reach = max(sp + num, reach)
                sp += 1
        if sp >= len(nums):
            return True
        return False