class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sq = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in sq or (cur,j) in sq or (i//3,j//3,cur) in sq:
                        return False
                    sq.add((i,cur))
                    sq.add((cur,j))
                    sq.add((i//3,j//3,cur))
        return True
