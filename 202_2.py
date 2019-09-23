class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        pre=float("inf")
        tmp=n
        while tmp!=pre:
            pre=tmp
            tmp=self.squresum(tmp)
            if tmp==1:
                return True
        return False



    def squresum(self,n):
        summ=0
        p=n
        while p:
            summ+=pow(p%10,2)
            p/=10
        return summ