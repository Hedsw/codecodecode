class Solution:
    # Time complexity is O(9^n)
    def solveSudoku(self, g: List[List[str]]) -> None:
        row = [[True]*9 for i in range(9)]        
        col = [[True]*9 for i in range(9)]
        sub = [[True]*9 for i in range(9)]  # 3*3 sub-box, from left to right, top to bottom.
        to_add = []
        for i in range(9):
            for j in range(9):
                if g[i][j] != '.':
                    d = int(g[i][j]) - 1
                    row[i][d] = col[j][d] = sub[i//3*3+j//3][d] = False
                else:
                    to_add.append((i, j))

        def backtrack():
            if not to_add: 
                return True
            i, j = to_add.pop()
            for d in range(9):
                if row[i][d] and col[j][d] and sub[i//3*3+j//3][d]:
                    g[i][j] = str(d+1)
                    row[i][d] = col[j][d] = sub[i//3*3+j//3][d] = False
                    if backtrack():
                        return True
                    g[i][j] = '.'
                    row[i][d] = col[j][d] = sub[i//3*3+j//3][d] = True
            to_add.append((i, j))
            return False

        backtrack()