# Palinedrome - 앞에서 읽으나 뒤에서 읽으나 똑같은 단어를 말함.. 예) 이박이, 오두오 이런것..

class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.boxs(s, i, i)
            if len(tmp) > len(answer):
                answer = tmp
            # Even case, like "abba"
            tmp = self.boxs(s, i, i+1)
            if len(tmp) > len(answer):
                answer = tmp
        return answer
            
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
    def boxs(self, s, left, right):
        while left >= 0 and right < len(s) and left <= len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
# 슬라이딩 윈도우 쓰면서 하는 것.. 그래서 O ( M * N )이 됨.. M 은 전체 str의 길이.. N은 while문에 들어간 것..
# Space Complexity -  O(1)


