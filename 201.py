class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a=self.rangeBitwiseAnd(m)
        b=self.rangeBitwiseAnd(n)
        return ~a&b

    def rangeInsersection(self,m):
        res=0
        for i in range(1,32):
            res+=pow(2,i-1)*(m/pow(2,i)%2)
        return res

