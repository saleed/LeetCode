class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s=="":
            return 0
        dp=[0]*len(s)
        for i in range(1,len(s)):
            if s[i]==")" and s[i-1]=="(":
                dp[i]=2

        for i in range(len(s)):
            if s[i]=="(":
                dp[i]=0
            else:
                if i-1-dp[i-1]>=0 and s[i-1-dp[i-1]]=="(":
                    dp[i]=dp[i-1]+2
                    if i-1-dp[i-1]-1>=0:
                        dp[i]+=dp[i-1-dp[i-1]-1]

        return max(dp)

a=Solution()
s =")()())"
print(a.longestValidParentheses(s))