class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0 for _ in range(n+1)]
        dp[0]=0
        dp[1]=0
        dp[2]=1
        for i in range(3,n+1):
            dp[i]=(i-1)*(dp[i-1]+dp[i-2])
        return dp[-1]






    def combine(self,n):
        ##排列组合，超时
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=0

        facRec=[1]*(n+1)
        for i in range(2,n+1):
            facRec[i]=self.fac(i)
            dp[i]=facRec[i]
            for j in range(1,i+1):
                dp[i]-=facRec[i]/facRec[i-j]/facRec[j]*dp[i-j]
            print(facRec)
        return int(dp[-1])%(math.pow(10,9)+7)



    def fac(self,i):
        res=1
        for i in range(1,i+1):
            res*=i
        return res


ss=Solution()
print(ss.findDerangement(2))