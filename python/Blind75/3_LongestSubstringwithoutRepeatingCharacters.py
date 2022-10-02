#슬라이딩 윈도우로 푸는 문제
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        sets = set()
        left = 0
        right = 0
        
        while left < len(s) and right < len(s):
            if s[right] not in sets:
                sets.add(s[right]) #Set을 써서.. 중복된 놈 있는지 확인 
                right += 1  # 슬라이딩 윈도우 오른쪽 이동      
                
                answer = max(answer, right - left) 
            else: # in sets
                sets.remove(s[left]) 
                left += 1 # 슬라이딩 윈도우 왼쪽 이동
        return answer
                
    # Sliding Window Problem
    # Time Complexity O(N)
    # Space Complexity O(k)
    # [k = length of the longest substring w/o repeating characters]