#刘汝佳的边境竞赛入门 有同样的题，本题未解决

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp=[[0 if i<j else 1 for i in range(len(s))] for j in range(len(s))]
        res=""
        for interval in range(len(s)):
            for i in range(len(s)):
                if interval==0:
                    dp[i][i]=1
                elif interval==1:
                    if i+1<len(s):
                        dp[i][i+1]=1 if s[i]==s[i+1] else 0

                else:
                    if i+interval<len(s):
                        dp[i][i+interval]=1 if dp[i+1][i+interval-1]==1 and s[i]==s[i+interval] else 0
                        res=s[i:i+interval+1]


        print(dp)


        return res

t1="abbba"
t2="abac"
a=Solution()
print(a.longestPalindrome(t1))
print(a.longestPalindrome(t2))