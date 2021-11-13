class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp2=[0 for _ in range(n+1)]
        dp5=[0 for _ in range(n+1)]
        for i in range(1,n+1):
            if i%2==0:
                dp2[i]=dp2[i/2]+1
            if i%5==0:
                dp5[i]=dp5[i/5]+1
        sum2=0
        sum5=0
        dp=(n+1)*[0]
        for i in range(n+1):
            sum2+=dp2[i]
            sum5+=dp5[i]
            dp[i]=min(sum2,sum5)
        # print(dp)
        return dp[n]



test=5
a=Solution()
print(a.trailingZeroes(test))