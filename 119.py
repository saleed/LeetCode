class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]

        res=[]
        fac_list=[]
        for i in range(rowIndex+1):
            fac_list.append(self.fac(i))
        for i in range(rowIndex+1):
            res.append(fac_list[rowIndex]/fac_list[rowIndex-i]/fac_list[i])
        return res


    def fac(self,j):
        if j==0:
            return 1
        res=1
        for k in range(1,j+1):
            res*=k
        return res


if __name__=="__main__":
    a=Solution()
    print(a.getRow(3))