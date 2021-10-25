class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """


        ret=[0]*rowIndex+1
        ret[0]=1
        for i in range(1,rowIndex+1):
            for j in reversed(range(1,i+1)):
                ret[j]=ret[j]+ret[j-1]

        return ret