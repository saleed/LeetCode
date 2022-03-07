class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.centerExpand(s)



    def dp(self, s):

        dp = [[bool(i >= j) for j in range(len(s))] for i in range(len(s))]

        maxstr = ""
        maxl = 0
        for l in range(0, len(s)):
            for i in range(len(s)):
                if i + l < len(s):
                    if i + 1 < len(s) and i+l-1>=0:
                        dp[i][i + l] = dp[i + 1][i + l - 1] and s[i] == s[i + l]
                    else:
                        dp[i][i + l]=(s[i] == s[i + l])
                    if l+1 > maxl and dp[i][i+l]:
                        maxstr = s[i:i + l + 1]
                        maxl = l+1
        return maxstr


    def centerExpand(self,s):
        maxl=0
        maxstr=""
        for i in range(len(s)):
            l=0
            while i-l>=0 and i+l<len(s) and s[i-l]==s[i+l]:
                if maxl <= l * 2 + 1:
                    maxstr = s[i - l:i + l+1]
                    maxl= l * 2 + 1
                l+=1

            l=0
            while i - l >=0 and i+ l+1 < len(s) and s[i - l] == s[i + l+1]:
                if maxl<=l * 2+2:
                    maxstr=s[i-l:i+l+2]
                    maxl = l * 2 + 2
                l += 1

        return maxstr

