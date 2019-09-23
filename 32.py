class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s)==0:
            return 0
        dp=[0]*len(s)

        dp[0]=0
        if s[:2]=='()':
            dp[1]=2


        for i in range(2,len(s)):
            if s[i]=='(':
                dp[i]=0
            else:
                if s[i-1]=='(':
                    dp[i]=dp[i-2]+2
                else:
                    # print(i-1-dp[i-1])
                    if i-dp[i-1]-1>=0 and s[i-1-dp[i-1]]=='(':
                        # print(111)
                        dp[i]=dp[i-1]+2
                        if i-dp[i-1]-2>=0:
                            dp[i]+=dp[i-dp[i-1]-2]
        print(dp)
        return max(dp)


a=Solution()
print(a.longestValidParentheses(")()())"))


print(a.longestValidParentheses("()(())"))

print(a.longestValidParentheses(")()())()()("))
