class Solution:
    def solveNQueens(self, n):
        t = ["."*i + "Q" + "."*(n-i-1) for i in range(n)]
        def dfs(queens, xy_dif, xy_sum):
            y = len(queens)
            if y==n:
                res.append(map(lambda x: t[x], queens))
                if not (n % 2 and queens[0] == n//2):
                    res.append(map(lambda x: t[~x], queens))
                return None
            if y == 0:
                for x in range(ceil(n/2.)):
                    if x not in queens and y-x not in xy_dif and y+x not in xy_sum: 
                        dfs(queens+[x], xy_dif+[y-x], xy_sum+[y+x])  
            else:
                for x in range(n):
                    if x not in queens and y-x not in xy_dif and y+x not in xy_sum: 
                        dfs(queens+[x], xy_dif+[y-x], xy_sum+[y+x])  
        res = []
        dfs([],[],[])
        return res
