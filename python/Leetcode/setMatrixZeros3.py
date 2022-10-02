class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        column = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    column.append(j) 
                    #set안에 row와 Col을 넣어주고..
        print(len(matrix[0]), len(matrix))

        for i in row: # Row가 있으면.. 그 로우에 있는 칼럼들 다 0
            for j in range(len(matrix[0])):
                matrix[i][j] = 0 # Col을 고정시키고, Raw를 쭉 0
        for i in column: # Col이 있으면.. 그 칼럼에 있는 로우들 다 0
            for j in range(len(matrix)): # Row를 고정시키고 Col을 쭉 0
                matrix[j][i] = 0 
        
        
        
    #Space Compelxity = O(n + m)
    #Time Comp O(m*n)