class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret=[0]*(rowIndex+1)
        for i in range(rowIndex+1):
            for j in range(i+1)[::-1]:
                if j==0 or j==i:
                    ret[j]=1
                else:
                    ret[j]=ret[j]+ret[j-1]
        return ret



