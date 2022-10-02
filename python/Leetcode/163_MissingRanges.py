class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower - 1] + nums + [upper + 1]
        ranges = []
        for index in range(1, len(nums)):
            if nums[index] - nums[index - 1] == 2:
                ranges.append(str(nums[index] - 1))
            elif nums[index] - nums[index - 1] > 2:
                ranges.append(str(nums[index - 1] + 1) + "->" + str(nums[index] - 1))
        return ranges

