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
        