class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.centerExpand(s)



    def centerExpand(self,s):

        center=0
        maxl=0
        res=""
        while center<len(s):
            p=center
            q=center
            while p>=0 and q<len(s) and s[p]==s[q]:
                if maxl < q - p + 1:
                    res = s[p:q + 1]
                    maxl = q - p + 1
                p-=1
                q+=1
            p=center
            q=center+1
            while p>=0 and q<len(s) and s[p]==s[q]:
                if maxl<q-p+1:
                    res=s[p:q+1]
                    maxl=q-p+1
                p-=1
                q+=1
            center+=1
        return res



    ##time limit exceed
    def dp(self, s):
        if len(s) <=1:
            return s

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(len(s)):
                if i >= j:
                    dp[i][j] = True
        maxl = 1
        res = ""

        for l in range(len(s)):
            for i in range(len(s)):
                if i + l >= len(s):
                    continue
                if l==0:
                    res=s[i]
                    continue
                if s[i ] == s[i + l] and dp[i + 1][i + l - 1]:
                    dp[i][i + l] = True
                    print(i,i+l,dp[i + 1][i + l - 1],dp[i][i + l] )
                    if l + 1 > maxl:
                        maxl = l + 1
                        res = s[i:i + l+1]
        return res








s="babad"
a=Solution()
print(a.longestPalindrome(s))