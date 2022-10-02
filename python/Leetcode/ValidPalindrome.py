class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        for i in s:
            if i.isalnum():
                filtered.append(i.lower())
        
        return filtered == filtered[::-1]