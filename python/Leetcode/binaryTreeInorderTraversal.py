# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS보다 BFS가 서칭 속도는 느리다. 특히나, 트리의 크기가 작은 곳에서는 DFS보다 BFS가 빠르다.
# BFS는 Preorder 방식이고, DFS는 Inorder 방식이다. 


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # 왼쪽 -> 중간 -> 오른쪽
        lists = []
        self.runner(root, lists)
        print(lists)
        return lists
        
    def runner(self, root, lists):
        if root:
            self.runner(root.left, lists)
            lists.append(root.val)
            self.runner(root.right, lists)
            # Time Complexity is O(V+E) V is vertex and E is edge - 리스트로 구현한 경우
            # Time Compleixty is O(V^2) V is vertex - 인접 행렬로 구현한 경우
            