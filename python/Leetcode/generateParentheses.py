# if right < left 인 이유..
# For the output string to be right, stack of ")" most be larger than stack of "(". If not, it creates string like "())"

# if not left and not right 인 이유..
# Since elements in each of stack are the same, we can simply express them with a number. For example, left = 3 is like a stacks ["(", "(", "("]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        self.dfs(res, n, n, "") # 여기에 n 을 두개 주고... 
        return res
        
    def dfs(self, res, left, right, path):
        
        if left > right or left < 0 or right < 0: # left > right 이거나, left < 0 이거나, right < 0 이거나..
            return 
        
        if left == 0 and right == 0: # 평소 같으면... len(nums) == 0 으로 할테지만, 이거는 두개니까.. 조건이 
            res.append(path)
            return
        
        self.dfs(res, left-1, right, path +'(' )
        self.dfs(res, left, right -1, path +')')
                 
"""
Time complexity is exponential 
The time complexity of DFS if the entire tree is traversed is O ( V ) O(V) O(V) where V is the number of nodes. In the case of a graph, the time complexity is O ( V + E ) O(V + E) O(V+E) where V is the number of vertexes and E is the number of edges.
"""