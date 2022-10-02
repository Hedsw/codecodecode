
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted1 = sorted(nums1)
        sorted2 = sorted(nums2)
        fast = slow = 0
        res = []
        
        while True:
            try:
                if sorted1[fast] == sorted2[slow]:
                    res.append(sorted1[fast])
                    fast += 1
                    slow += 1
                    
                elif sorted1[fast] < sorted2[slow]:
                    fast += 1
                else:
                    slow += 1
            except:
                break
        return res