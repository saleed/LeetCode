class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        return self.titleToNumber(s[:-1])*26+(ord(s[-1])-ord('A')+1)
