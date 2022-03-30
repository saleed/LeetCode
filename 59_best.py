class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        board = [[0 for _ in range(n)] for _ in range(n)]
        cnt = 1
        for i in range(n / 2 + 1):
            for j in range(n - 2 * i - 1):
                board[i][i + j] = cnt
                cnt += 1
            for j in range(n - 2 * i - 1):
                board[i + j][n - 1 - i] = cnt
                cnt += 1
            for j in range(n - 2 * i - 1):
                board[n - 1 - i][n - 1 - i - j] = cnt
                cnt += 1
            for j in range(n - 2 * i - 1):   ###注意需要是range(n-2*i-1)
                board[n - 1 - i - j][i] = cnt
                cnt += 1
        if n % 2:   ##注意这种情况
            board[n / 2][n / 2] = n * n

        return board


