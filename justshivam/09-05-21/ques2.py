class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        arr = grid[0]
        for x in range(1, n):
            arr[x] += arr[x-1]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    arr[j] += grid[i][j]
                else:
                    arr[j] = min(arr[j-1], arr[j]) + grid[i][j]
        return arr[-1]
