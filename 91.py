class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.dfs(s)

    def dfs(self, s):
        if len(s)==0:
            return 1
        if len(s) == 1:
            return int(s[0]>'0')
        return int(s[0]>'0')*self.dfs(s[1:])+int(s[0]>'0' and s[:2]<='26')*self.dfs(s[2:])
