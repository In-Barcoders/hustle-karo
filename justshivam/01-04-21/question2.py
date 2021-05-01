class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.row = defaultdict(list)
        self.col = defaultdict(list)
        self.square = defaultdict(list)
        self.board = board
        count = 0

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != ".":
                    number = int(self.board[i][j])
                    self.row[i].append(number)
                    self.col[j].append(number)
                    self.square[(i//3, j//3)].append(number)
                    count += 1

        self.backtrack(count)
        return

    def backtrack(self, count) -> bool:
        if count == 81:
            return True
        curr_min = (float("inf"), [], [])
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == ".":
                    curr_possible = set(
                        list(range(1, 10))) - set(self.row[i]+self.col[j] + self.square[(i//3, j//3)])
                    if curr_min[0] > len(curr_possible):
                        curr_min = (len(curr_possible),
                                    list(curr_possible), [i, j])

        for x in curr_min[1]:
            self.board[curr_min[2][0]][curr_min[2][1]] = str(x)
            self.row[curr_min[2][0]].append(x)
            self.col[curr_min[2][1]].append(x)
            self.square[(curr_min[2][0]//3, curr_min[2][1]//3)].append(x)
            if self.backtrack(count+1):
                return True
            self.board[curr_min[2][0]][curr_min[2][1]] = "."
            self.row[curr_min[2][0]].remove(x)
            self.col[curr_min[2][1]].remove(x)
            self.square[(curr_min[2][0]//3, curr_min[2][1]//3)].remove(x)
        return False
