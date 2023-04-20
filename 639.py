class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp=[0]*(len(s)+1)
        if s[0]!="*":
            dp[1]=9
        elif s[0]!='0':
            dp[1]=1
        else:
            return 0
        for i in range(2,len(s)+1):
            if s[i-1]=="*":
                dp[i]=9*(dp[i-2]+dp[i-1])
            else:

                if s[i-1]!="0" :
                    dp[i]+=dp[i-1]
                if s[i-2]!='0' and 1<=int(s[i-2:i])<=26:
                    dp[i]+=dp[i-2]

            if dp[i]==0:
                return 0

        return int(dp[-1]/(math.pow(10, 9) + 7))


ss=Solution()
print(ss.numDecodings())