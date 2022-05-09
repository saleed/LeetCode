class Solution(object):
    def longestLine(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        dp = [[[0 for _ in range(4)] for _ in range(len(mat[0]))] for _ in range(len(mat))]

        maxv = -float("inf")
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == 0 and j == 0:
                    dp[i][j] = [1, 1, 1] if mat[i][j] == 1 else [0, 0, 0]
                elif i == 0:
                    if mat[i][j] == 1:
                        dp[i][j][0] = 1
                        dp[i][j][1] = dp[i][j - 1][1] + 1
                        dp[i][j][2] = 1
                        dp[i][j][3] = 1

                elif j == 0:
                    if mat[i][j] == 1:
                        dp[i][j][0] = dp[i - 1][j][0] + 1
                        dp[i][j][1] = 1
                        dp[i][j][2] = 1
                        dp[i][j][3] = dp[i - 1][j + 1][3] + 1 if j + 1 < len(mat[0]) else 1
                else:
                    if mat[i][j] == 1:
                        dp[i][j][0] = dp[i - 1][j][0] + 1
                        dp[i][j][1] = dp[i][j - 1][1] + 1
                        dp[i][j][2] = dp[i - 1][j - 1][2] + 1
                        dp[i][j][3] = dp[i - 1][j + 1][3] + 1 if j + 1 < len(mat[0]) else 1

                maxv = max(maxv, max(dp[i][j]))
        return maxv
