"""
s = "abc", shifts = [3,5,9]
Output: "rpl"

After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

This is equivalent to shifting "abc" with shifts=[3+5+9 , 5+9 , 9 ] == [17 , 14 , 9]

We observe that we have to maintain a reverse prefix sum of the shifts array and this will be equal to the number of shifts for each character.

ASCII values for:
'a'=97
'b'=98
'c'=99

"""
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        for i in range(n-2, -1, -1):
            shifts[i] = (shifts[i] + shifts[i+1]) % 26
            
        ans = []
        for i, c in enumerate(s):
            idx = (ord(c) - ord('a') + shifts[i]) % 26
            ans.append(chr(idx + ord('a')))
        return "".join(ans)
"""
Complexity

Time: O(N), where N <= 10^5 is length of string s.
Space:
Python: O(N)
"""