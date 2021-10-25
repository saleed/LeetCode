class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        ret=[0]*numRows
        res=[]
        ret[0]=1
        res.append(ret[:1])
        for i in range(1,numRows):
            for j in reversed(range(1,i+1)):
                ret[j]=ret[j]+ret[j-1]
            res.append(ret[:i+1])
        return  res