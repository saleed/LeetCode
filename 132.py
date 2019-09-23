class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        dp=[float("inf")]*len(s)
        plm=self.palindromeMatrix(s)
        for i in range(len(s)):
            if plm[0][i]==1:
                dp[i]=0
            else:
                for j in range(i):
                    if  plm[j+1][i]:
                        dp[i]=min(dp[j]+1,dp[i])
        print(dp)
        return dp[len(s)-1]

    def palindromeMatrix(self,s):
        l=len(s)
        plm=[[0 for _ in range(l)] for _ in range(l)]
        for interval in range(l):
            for start in range(l):
                if interval==0:
                    plm[start][start+interval]=1
                elif start+interval<l:
                    if (plm[start+1][start+interval-1]==1 or start+interval-1<start+1)and s[start]==s[start+interval]:
                        plm[start][start+interval]=1
        for i in range(l):
            print(plm[i])
        return plm




a=Solution()
test="aab"
print(a.minCut(test))
test="leet"
print(a.minCut(test))


