# Time Comp - O(M*N) where n = number of rows * number of cols
# Space Comp - O(1)
class Solution:
    def spiralOrder2(self, matrix):
        """
        Initially, we move by the RIGHT direction.
        If we meet the boundary or we meet visited cell then we change to the next direction.
        Directions are in order [RIGHT, DOWN, LEFT, TOP].
        We iterate m*n times to add m*n cells to our anser.
        """
        m, n, VISITED = len(matrix), len(matrix[0]), 999
        DIR = [0, 1, 0, -1, 0]  # (r + DIR[i], c + DIR[i+1]) corresponding to move [RIGHT, DOWN, LEFT, TOP]
        r, c, d = 0, 0, 0
        ans = []
        for _ in range(m * n):
            nr, nc = r + DIR[d], c + DIR[d+1]
            if not 0 <= nr < m or not 0 <= nc < n or matrix[nr][nc] == VISITED:  # If out of bound or already visited
                d = (d + 1) % 4  # Change next direction
                nr, nc = r + DIR[d], c + DIR[d+1]

            ans.append(matrix[r][c])
            matrix[r][c] = VISITED  # Mark as visited
            r, c = nr, nc

        return ans