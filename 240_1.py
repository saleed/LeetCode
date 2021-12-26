class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        cornor=[0,len(matrix[0])-1]
        while cornor[0]<len(matrix) and cornor[1]>=0:
            if matrix[cornor[0]][cornor[1]]==target:
                return True
            elif target<matrix[cornor[0]][cornor[1]]:
                cornor[0]-=1
            else:
                cornor[1]+=1
        return False
