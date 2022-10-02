# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS보다 BFS가 서칭 속도는 느리다. 특히나, 트리의 크기가 작은 곳에서는 DFS보다 BFS가 빠르다.
# BFS는 Preorder 방식이고, DFS는 Inorder 방식이다. 


# Deque를 사용했기 때문에 이것에 대한 Time Complexity는 O(n)이다 
#Using single ended queue and initializing array instead of reversing.

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        even_level = False
        queue = collections.deque([root])
        
        while queue:
            n = len(queue)
            level = [0] * n
            for i in range(n):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # to maintain the order of nodes in the format of [left, right, left, right] 
                if even_level:
                    level[n-1-i] = node.val
                else:
                    level[i] = node.val
            res.append(level)
            even_level = not even_level
        return res
        
            
            