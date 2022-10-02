# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
if not root:
    return 

IS SAME WITH BELOW

if root is None 
    return
'''
#DFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []       
        res = []
        self.dfs(root, res, 0)
        
        return res
        
    def dfs(self, root, res, level):
        if root is None:
            return 
        
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        
        self.dfs(root.left, res, level + 1)
        self.dfs(root.right, res, level + 1)
        
          