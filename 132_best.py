class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        huiwen=self.isHuiWen(s)
        return self.ditui(huiwen,s)

    def isHuiWen(self,s):
        dp=[[i>=j for j  in range(len(s))] for i in range(len(s))]

        for itv in range(1,len(s)):
            for i in range(len(s)-1):
                if i+itv<len(s) and dp[i+1][i+itv-1] and s[i]==s[i+itv] :
                    dp[i][i+itv]=True
        print(dp)
        return dp

    def ditui(self,huiwen,s):
        dp=[float("inf") for _ in range(len(s)+1)]
        dp[0]=0
        for i in range(1,len(s)+1):
            if huiwen[0][i-1]:
                dp[i]=0
            else:
                for j in range(i):
                    if huiwen[j][i-1]:
                        dp[i]=min(dp[i],dp[j]+1)
        print(dp)
        return dp[-1]




test="aab"
aaa=Solution()
print(aaa.minCut(test))