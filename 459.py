class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for l in range(1,len(s)):
            if len(s)%l!=0:
                continue
            p=0
            tmp=s[p:p+l]
            while p+l<=len(s) and s[p:p+l]==tmp:
                p+=l
            if p+l<=len(s):
                continue
            else:
                return True
        return False