class Solution:
    # Time Complexity : O(NlogN), where N is the number of elements in nums
    # Space Complexity : O(1), ignoring the space required by sorting algorithm.
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest, cur_longest = 0, min(1, len(nums))
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] : continue
            if nums[i] == nums[i - 1] + 1: cur_longest += 1
            else: longest, cur_longest = max(longest, cur_longest), 1
        return max(longest, cur_longest)
    
    # Time Complexity : O(N)
    # Space Complexity : O(N)
    def longestConsecutive2(self, nums: List[int]) -> int:
        longest, s = 0, set(nums)
        for num in nums:
            cur_longest, j = 1, 1
            while num - j in s: 
                s.remove(num - j)
                cur_longest, j = cur_longest + 1, j + 1
            j = 1
            while num + j in s: 
                s.remove(num + j)
                cur_longest, j = cur_longest + 1, j + 1
            longest = max(longest, cur_longest)
        return longest