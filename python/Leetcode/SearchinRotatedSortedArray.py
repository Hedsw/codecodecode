class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search 만든 것.. 그냥 바이너리서치로 구하면 됨. 바이너리서치는 O(log n)
        # Time Complexity - O(log n). 
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
    