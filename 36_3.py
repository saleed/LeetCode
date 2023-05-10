class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        for i in range(len(board[0])):
            s = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] in s:
                    return False
                s.add(board[j][i])

        for i in range(9):
            s = set()
            for j in range(9):
                x = (i / 3) * 3 + j / 3
                y = (i % 3) * 3 + j % 3
                if board[x][y] == '.':
                    continue
                if board[x][y] in s:
                    return False
                s.add(board[x][y])
        return True
