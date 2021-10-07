#2019年提交的额代码

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        res=[]
        for i in range(rowIndex+1):
            res.append([1]*(i+1))
            for j in range(1,i):
                res[i][j]=res[i-1][j]+res[i-1][j-1]
        return res[-1]