class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n<5:
            return 0



        dp5=[0]*(n+1)
        dp5[5]=1
        for i in range(n+1):
            if i%5==0:
                dp5[i]=dp5[i/5]+1
        return sum(dp5)