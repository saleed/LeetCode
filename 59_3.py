class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        board = [[-1 for _ in range(n)] for _ in range(n)]
        count = 0
        row = 0
        col = -1
        while count < n * n:
            print(board)
            while col + 1 < n and board[row][col + 1] == -1:
                col += 1
                count += 1
                board[row][col] = count
            while row + 1 < n and board[row + 1][col] == -1:
                row += 1
                count += 1
                board[row][col] = count
            while col - 1 >= 0 and board[row][col - 1] == -1:
                col -= 1
                count += 1
                board[row][col] = count
            while row - 1 >= 0 and board[row - 1][col] == -1:
                row -= 1
                count += 1
                board[row][col] = count
        return board




