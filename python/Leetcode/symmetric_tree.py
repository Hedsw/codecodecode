# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.checker(root.left, root.right)
    
    def checker(self, left, right):
        
        if left is None and right is None:
            return True
        
        if left is None or right is None:
            return False
        
        if left.val == right.val:
            outvalue = self.checker(left.left, right.right)
            invalue = self.checker(left.right, right.left)
            return outvalue and invalue
        return False 