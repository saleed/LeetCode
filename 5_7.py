class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        maxl=1
        maxstr=""
        for i in range(len(s)):
            p=i-1
            q=i+1
            l=0
            while p>=0 and q<len(s) and s[p]==s[q]:
                l+=2
                if l>maxl:
                    maxl=l
                    maxstr=s[p:q+1]
                p-=1
                q+=1

        for i in range(len(s)-1):
            p=i
            q=i+1
            l=0
            while p>=0 and q<len(s) and s[p]==s[q]:
                l+=2
                if l > maxl:
                    maxl = l
                    maxstr = s[p:q + 1]
                p-=1
                q+=1
        return maxstr




