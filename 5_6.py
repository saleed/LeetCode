class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        maxl=1
        res=[0,0]
        for mid in range(len(s)):
            p=mid-1
            q=mid+1
            while p>=0 and q<len(s):
                if s[p]==s[q]:
                    p-=1
                    q+=1
                    res=[p,q] if 1+q-p>maxl else res
                    maxl=max(maxl,q-p+1)
                else:
                    break
            p=mid
            q=mid+1
            while p>=0 and q<len(s):
                if s[p]==s[q]:
                    p-=1
                    q+=1
                    res=[p,q] if 1+q-p>maxl else res
                else:
                    break
        return s[res[0]:res[1]+1]
