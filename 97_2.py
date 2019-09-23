class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        # return self.dfs(s1,s2,s3,0,0)
        return self.dp(s1,s2,s3)


    #超时
    def dfs(self,s1,s2,s3,p,q):
        if p==len(s1) and q==len(s2):
            return True
        if p<len(s1) and s1[p]==s3[p+q] and self.dfs(s1,s2,s3,p+1,q):
            return True
        if q<len(s2) and s2[q]==s3[p+q] and self.dfs(s1,s2,s3,p,q+q):
            return True
        return False

    def dp(self,s1,s2,s3):
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[False for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
        dp[0][0]=True
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    dp[i][j]=True
                elif i==0:
                    dp[i][j]=dp[i][j-1] and s3[i+j-1]==s2[j-1]
                elif j==0:
                    dp[i][j] = dp[i - 1][j] and s3[i+j-1] == s1[i-1]
                else:
                    dp[i][j]=(dp[i-1][j] and s3[i+j-1]==s1[i-1]) or (dp[i][j-1] and s3[i+j-1]==s2[j-1])
        return dp[-1][-1]



