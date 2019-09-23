class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        x=0
        y=len(matrix[0])-1
        while x<len(matrix) and y>=0:

            while y>=0 and matrix[x][y]>target:
                y-=1
            while x<len(matrix) and matrix[x][y]<target:
                x+=1
            if y>=0 and x<len(matrix) and matrix[x][y]==target:
                return True
        return False
