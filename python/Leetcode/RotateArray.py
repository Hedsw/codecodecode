
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        front = []
        back = []
        
        for i in range(0, len(nums)-k):
            front.append(nums[i])
        
        for i in range(len(nums)-k, len(nums)):
            back.append(nums[i])
        
        new = back + front
        
        for i in range(len(nums)):
            nums[i] = new[i]
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        print(k)
        nums[:] = nums[-k:] + nums[:-k]
'''