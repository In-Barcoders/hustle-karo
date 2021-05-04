def isValidSudoku(self, board: List[List[str]]) -> bool:
    for i in range(9):
        arrR = []
        arrC = []
        for j in range(9):
            if board[i][j] != '.':
                if not board[i][j] in arrR:
                    arrR.append(board[i][j])
                else:
                    return False
            if board[j][i] != '.':
                if not board[j][i] in arrC:
                    arrC.append(board[j][i])
                else:
                    return False
    for i in range(2, 9, 3):
        for j in range(2, 9, 3):
            cur = []
            for k in range(3):
                for l in range(3):
                    if board[i-k][j-l] != '.':
                        if not board[i-k][j-l] in cur:
                            cur.append(board[i-k][j-l])
                        else:
                            return False
    return True
