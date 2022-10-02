class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        sets = set()
        length = len(s)
        right, left = 0, 0
        answers = []
        while right < length and left < length:
            if s[right] not in sets:
                sets.add(s[right])
                print(sets, " ADD")
                right += 1
                answer = max(answer, right - left)
        # 만약.. 제일 큰 자리를 뽑아내려면.. 아래와 같이 List에 넣어준 다음.. 나중에 Length 비교해서 제일 큰 것들 뽑아내면 됨
            """    
                if answer <= right-left:
                    answers.append(s[left: right])    
            """
            else:
                sets.remove(s[left])
                print(sets, " Remove")
                left += 1
        """
        print(answers)
        """
        return answer
                
    # Sliding Window Problem
    # Time Complexity O(N)
    # Space Complexity O(k)
    # [k = length of the longest substring w/o repeating characters]
