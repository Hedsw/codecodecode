# Time Complexity: O(N^2) where N is the length of each side of the matrix
# Space Complexity: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # reverse
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        # transpose 
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
# Rotate을 하기 위해서는.. Reverse -> Transpose 를 하면 Rotate가 됨
# Transposing means: rows become columns, columns become rows.
# Reversing the matrix does this: