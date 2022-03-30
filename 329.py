class Solution(object):
    def longestIncreasingPath(self, matrix):
        matrix = {i + j * 1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}
        length = {}
        print(sorted(matrix, key=matrix.get))
        # print(matrix.get())
        for

        for z in sorted(matrix, key=matrix.get):
            length[z] = 1 + max([length[Z]
                                 for Z in [z + 1, z - 1, z + 1j, z - 1j]
                                 if Z in matrix and matrix[z] > matrix[Z]]
                                or [0])
        return max(length.values() or [0])
    #come up with some new question
    #1.
    #2.the max path weight in the matrix: how to solove it


nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
a=Solution()
a.longestIncreasingPath(nums)



