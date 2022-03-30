class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        area=-float("inf")
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                area=1

        for i in range(len(matrix[0])):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                area = 1


        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "0":
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                area=max(area,dp[i][j])
        return area*area



