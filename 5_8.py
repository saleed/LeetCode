class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxl=1
        maxstr=""
        for i in range(len(s)):
            p=i
            q=i
            while p>=0 and q<len(s) and s[p]==s[q]:
                if q-p+1>maxl:
                    maxl=q-p+1
                    maxstr=s[p:q+1]
                p-=1
                q+=1
        for i in range(len(s)-1):
            p=i
            q=i+1
            while p>=0 and q<len(s) and s[p]==s[q]:
                if q - p + 1 > maxl:
                    maxl = q - p +1
                    maxstr = s[p:q + 1]
                p-=1
                q+=1
        return maxstr


s="ccc"
a=Solution()
print(a.longestPalindrome(s))