class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        mt={i+1j: val for i,row in range(len(matrix)) for j,val in row}
