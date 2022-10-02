class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        #nums.reverse()
        
        return nums[k-1]
    
# Time Complexity is.. O(n. logn) 파이썬은 Timsort algorithm since version 2.3 쓴다.