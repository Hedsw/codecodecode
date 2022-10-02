# Time Complexity : O(N), more specifically, within the range [L, H]
# Space Complexity : O(H)

class Solution:
    def rangeSumBST(self, root, L, H):
        if not root: return 0
        ans = root.val if root.val >= L and root.val <= H else 0
        if root.val > L: ans += self.rangeSumBST(root.left, L, H)
        if root.val < H: ans += self.rangeSumBST(root.right, L, H)
        return ans