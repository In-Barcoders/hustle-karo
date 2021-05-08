class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        res = [[0 for i in range(n)] for j in range(n)]
        cnt = 1
        for i in range((n+1)//2):
            for j in range(i, n-i):
                res[i][j] = cnt
                cnt += 1
            for j in range(i+1, n-i):
                res[j][n-i-1] = cnt
                cnt += 1
            for j in range(i+1, n-i):
                res[n-i-1][n-j-1] = cnt
                cnt += 1
            for j in range(i+1, n-i-1):
                res[n-j-1][i] = cnt
                cnt += 1
        return res
