class Solution:
    def sortColors(self, nums): # three pointer
        left, right, mid = 0, len(nums) - 1, 0
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                mid += 1
                left +=1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
# Time Complexity - O(1)