class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0] * len(s)

        for i in range(len(s)):
            if s[i] == "(":
                dp[i] = 0
            else:
                if i - 1 >= 0 and i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == "(":
                    dp[i] = 2 + dp[i - 1]
                    if i - 1 - dp[i - 1] - 1 >= 0:
                        dp[i] += dp[i - 1 - dp[i - 1] - 1]

        print(dp)
        return max(dp)



