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

        while not(x>=len(matrix) or y<0):
            print(x,y)
            if matrix[x][y]<target:
                x+=1
            elif matrix[x][y]>target:
                y-=1
            else:
                return True
        return False
test=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
t=3
a=Solution()
print(a.searchMatrix(test,t))