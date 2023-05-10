class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        cnt = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        maxl = min(len(matrix), len(matrix[0]))
        nr = len(matrix)
        nc = len(matrix[0])
        for i in range((maxl + 1) / 2):
            for j in range(i, nc - i):
                matrix[i][j] = cnt
                cnt += 1
            for j in range(i + 1, nr - i):
                matrix[j][nc - i - 1] = cnt
                cnt += 1
            for j in range(i, nc - i - 1)[::-1]:
                matrix[nr - i - 1][j] = cnt
                cnt += 1
            for j in range(i + 1, nr - i - 1)[::-1]:
                matrix[j][i] = cnt
                cnt += 1
        return matrix
