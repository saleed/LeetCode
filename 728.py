class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for i in range(left,right+1):
            if self.selfdiv(i):
                res.append(i)
        return res



    def selfdiv(self,n):
        l=n
        while l:

            if l%10==0 or n%(l%10)>0:
                return False
            l/=10
        return True
