class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for r0 in range(n//2):
            for c0 in range(n//2 + n%2):
                r2, c2 = n-r0-1, n-c0-1
                r1, c1 = n-c2-1, r2
                r3, c3 = n-c0-1, r0
                matrix[r0][c0], matrix[r1][c1], matrix[r2][c2], matrix[r3][c3] = matrix[r3][c3], matrix[r0][c0], matrix[r1][c1], matrix[r2][c2]
