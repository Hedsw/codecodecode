class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        #s, t = 0, len(nums) - 1
        result = []

        # Check Duplication
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            value = nums[i] * -1 # Three Summary reduced to two Summary -> a + b = -c로 하면 3개 합을 2개 합으로 줄일 수 있음.
            s, t = i+1, len(nums) - 1
            while s < t:
                if nums[s] + nums[t] == value: #이게 3개 합이 2개합으로 줄인 것
                    result.append([nums[i], nums[s], nums[t]])
                    s = s + 1
                    while s < e and nums[s] == nums[s-1]: #이거 [0,0,0] 경우 예외 케이스
                        s = s + 1
                elif nums[s] + nums[t] < value:
                    s = s + 1
                else:
                    t = t - 1
        return result
            
        