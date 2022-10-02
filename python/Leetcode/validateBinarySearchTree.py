# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        if root is None:
            return True
        array = []
        self.inorder(root, array)
        
        for i in range(len(array)-1):
            if array[i] >= array[i+1]:
                return False
        return True
    
    def inorder(self, root, array):
        if root is None:
            return 
        
        self.inorder(root.left, array)
        array.append(root.val)
        self.inorder(root.right, array)