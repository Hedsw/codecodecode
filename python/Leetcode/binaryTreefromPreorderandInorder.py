# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        res = []
        if root is None:
            return res
        
        
    def inordertree(self, root, res):
        
        inordertree(root.left, res)
        if root is not None:
            res.append(root.val)
        inordertree(root.right, res)
        
        
    def preordertree(self, root, res):
        
        if root is not None:
            res.append(root.val)
        
        preodertree(root.left, res)
        preordertree(root.right, res)
        