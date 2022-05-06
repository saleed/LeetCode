class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """


        dp=[[1 if i==j else 0 for j in range(len(s))] for i in range(len(s))]

        for l in range(1,len(s)):
            for i in range(len(s)):
                if i+l<len(s):
                    if s[i]==s[i+l]:
                        dp[i][i+l]=dp[i+1][i+l-1]+2
                    else:
                        dp[i][i+l]=max(dp[i+1][i+l],dp[i][i+l-1])
        return dp[0][-1]
