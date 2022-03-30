class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        dp=[[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

        if len(s1)+len(s2)!=len(s3):
            return False

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    dp[i][j]=1
                elif i==0:
                    dp[i][j]=1 if s3[i+j-1]==s2[j-1]  and dp[i][j-1]==1 else 0
                elif j==0:
                    dp[i][j]=1 if s3[i+j-1]==s1[i-1] and dp[i-1][j] ==1 else 0
                else:
                    dp[i][j]=1 if (s3[i+j-1]==s1[i-1] and dp[i-1][j] ==1 )or (s3[i+j-1]==s2[j-1]  and dp[i][j-1]==1) else 0
        return dp[-1][-1]==1