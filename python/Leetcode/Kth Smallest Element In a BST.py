class Solution(object):
    # Time complexity - O(nlogn)
    # Space Complexity - O(d) - d is max depth of recursion
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        self.helper(root, res)
        res = sorted(res)
        print(res)
        return res[k-1]
    def helper(self, root, res):            
        if root is None:
            return
         
        res.append(root.val)
         
        self.helper(root.left, res)
        self.helper(root.right, res)
        
        #Time complexity: O(N), Space complexity is O(d) - d is the max depth of recursion.
    def kthSmallest2(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)
        
        #위에 방법은 안에서 찾는 방법임 