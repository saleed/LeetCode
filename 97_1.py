class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        dp=[[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]


        for i in range(0,len(s1)+1):
            for j in range(0,len(s2)+1):
                if i==0 and j==0:
                    dp[0][0]=1
                if i>0 and dp[i-1][j]==1 and s1[i-1]==s3[i+j-1]:
                    dp[i][j]=1
                if j>0 and dp[i][j-1]==1 and s2[j-1]==s3[i+j-1]:
                    dp[i][j]=1
        for v in dp:
            print(v)
        return dp[-1][-1]


s1="aabcc"
s2="dbbca"
s3="aadbbcbcac"
a=Solution()
print(a.isInterleave(s1,s2,s3))
