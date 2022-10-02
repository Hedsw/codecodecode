class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i,j, word):
                    return True
        return False
    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # All of words are checked
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): # Out of Range
            return False
        
        if board[i][j] != word[0]:
            return False
        
        tmp = board[i][j] # first character is found, check the remaining part
        board[i][j] = '#' # avoid visit agian  
        
        # check whether can find "word" along one direction

        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        
        board[i][j] = tmp
        return res
    '''
    Time complexity is mn4^len(s).
A worst case is matching all the characters except the last one. => len(s)
How many boxes in a board => m * n
How many directions for a box => 4
So the worst case is I travel all the boxes and four directions on every box and all directions' the last character are not correct. (remember we have a record for visited boxes. )v
    
    '''