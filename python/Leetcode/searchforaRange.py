class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Bisect는 바이너리 서치이기 때문에 O(log(n))이다
        # 0 일 때 예외처리
        if len(nums) == 0:
            return [-1, -1]
        
        left = bisect_left(nums, target)
        print(left)
        if left != len(nums) and nums[left] == target:
            pass
        else:
            left = -1
        
        right = bisect_right(nums, target)
        print(right)
        if right != len(nums) + 1 and nums[right - 1] == target:
            pass
        else:
            right = -1
        
        # 둘 다 자리 없을 때, 그냥 -1 로 내는거 예외처리
        if right == -1 and left == -1:
            return [left, right]
        # 둘 다 자리 있을 경우.. 참고로 right - 1은 right가 원래 내보내는 자리가 우리가 찾는 곳의 Index + 1로 해주기 때문에
        else:
            return [left, right-1]
    
    