class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)>len(s):
            return False
        if len(s)==len(p):
            return True




    def Match(self,s,p,pre):
        if pre=="":
            if p=='.':
                return self.Match(s[1:],p[1:],'.')
            else:
                return False
        elif pre=='.':

        elif pre==