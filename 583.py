class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp=[[float("inf") for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                else:
                    if word1[i-1]==word2[j-1]:
                        dp[i][j]=min(dp[i-1][j-1],dp[i-1][j]+1,dp[i][j-1]+1)
                    else:
                        dp[i][j]=min(dp[i - 1][j - 1]+2, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
            print(dp[i])
        return dp[-1][-1]

a="leetcode"
b="etco"
ss=Solution()
print(ss.minDistance(a,b))
