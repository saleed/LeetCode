class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p=0
        q=0
        while p<len(s) and q<len(t):
            if t[q]==s[p]:
                p+=1
            q+=1
        if q==len(t) and p<len(s):
            return False
        return True
