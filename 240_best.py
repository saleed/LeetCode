class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        x=0
        y=len(matrix[0])-1
        while x<len(matrix) and y>=0:
            if matrix[x][y]<target:
                x+=1
            elif matrix[x][y]>target:
                y-=1
            else:
                return True
        return False