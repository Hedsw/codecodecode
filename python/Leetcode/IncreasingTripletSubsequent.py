
    # 제일 큰 작은 숫자부터 threshold1에 넣고, 그 다음 작은 숫자를 threshold2에 넣고 계속적으로 숫자를 늘려가면 됨
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        
        for num in nums:
            if first >= num:
                first = num
            elif second >= num:
                second = num
            else:
                return True
        return False
    
    
    
    
    