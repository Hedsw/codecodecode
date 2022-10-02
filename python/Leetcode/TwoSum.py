class Solution:
    # two for loop -> O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i, length):
                if i != j and  nums[j] + nums[i] == target:
                    return [i,j]
    # Hash map 써서.. O(n),이고 Space complexity -> O(n)             
    def twoSum2(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
