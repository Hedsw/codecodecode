class Solution:
    # Sol 1 -> Time compleixty - O(nlogn) N is height M is descending of Height 
    # Sorting과 비슷한 Time Complexity를 보여줌 
    # Space Complexity - O(n) List를 쓰니까..
    def maxArea1(self, height: List[int]) -> int:
        
        # 양쪽에서 하나씩 해서.. list에 더해서 max인거 빼내기..?
        ans = []
        l = 0
        r = len(height) - 1
        
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                # J 는 오른쪽, I 는 왼쪽
                if height[j] > height[i]:
                    ans.append(height[i] * (j - i))
                else:
                    ans.append(height[j] * (j - i))
        return max(ans)
                    
    #Time Comp - O(N)
    #Space - O(1)
    def maxArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res