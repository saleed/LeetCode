class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        dp=[[0 for _ in  range(len(t))] for _ in range(len(s))]


        for i in range(len(s)):
            for j in range(len(t)):
                if i==0 and j==0:
                    dp[i][j]=1 if s[0]==t[0] else 0
                elif i==0:
                    dp[i][j]=0
                elif j==0:
                    dp[i][j]=dp[i-1][j]
                else:
                    if s[i]==t[j]:
                        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                    else:
                        dp[i][j]=dp[i-1][j]
        return dp[-1][-1]

