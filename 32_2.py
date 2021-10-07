class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0

        dp=[0 for _ in range(len(s))]
        for i in range(1,len(s)):
            if s[i]=="(":
                dp[i]=0
            else:
                if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=="(":
                    dp[i]=dp[i-1]+2
                    if i-dp[i-1]-2>=0:
                        dp[i]+=dp[i-dp[i-1]-2]



        print(dp)
        return max(dp)







if __name__=="__main__":
    a=Solution()
    test="(()()"
    print(a.longestValidParentheses(test))

