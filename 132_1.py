class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        huiwen=self.isHuiWen(s)
        #
        # res=[float("inf")]
        # self.dfs(res,0,0,s,huiwen)
        # return res[0]-1

        ret=self.dpSolve(s,huiwen)
        return ret


    def isHuiWen(self,s):
        huiwen=[[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(len(s)):
                if i+j<len(s) and i-j>=0 and s[i+j]==s[i-j]:
                    huiwen[i-j][i+j]=True
                else:
                    break

            for j in range(len(s)):
                if i+j+1<len(s) and i-j>=0 and s[i+j+1]==s[i-j]:
                    huiwen[i-j][i+j+1]=True
                else:
                    break

        return huiwen

####time limit
    def dfs(self,res,tmp,i,s,huiwen):
        # print(tmp,i)
        if i>=len(s):
            res[0]=min(res[0],tmp)
            return
        for p in range(i,len(s)):
            if huiwen[i][p]:
                self.dfs(res,tmp+1,p+1,s,huiwen)

####
    def dpSolve(self,s,huiwen):
        dp=[float("inf")]*len(s)
        for i in range(len(s)):
            for j in range(i+1):
                if huiwen[j][i]:
                    if j-1>=0:
                        dp[i]=min(dp[i],dp[j-1]+1)
                    else:
                        dp[i]=min(dp[i],0)
        return dp[-1]




a=Solution()
test="abbaab"
for v in a.isHuiWen(test):
    print(v)

print(a.minCut(test))