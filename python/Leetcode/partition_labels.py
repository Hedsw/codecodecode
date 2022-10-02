class Solution:
    # TC = O(N)
    def partitionLabels(self, s: str) -> List[int]:
        d = collections.defaultdict(int)
        for i, c in enumerate(s):
            d[c] = i
                
        ans, left, right = [], -1, -1
            
        for i,c in enumerate(s):
            right = max(right, d[c])
            
            if i == right:
                ans.append(right - left)
                left = i
        return ans
    
# Figure out the rightmost index first and use it to denote the start of the next section.
# Reset the left pointer at the start of each new section.
# Store the difference of right and left pointers + 1 as in the result for each section.

