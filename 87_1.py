class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)!=len(s2) or set(s1)!=set(s2):
            return False
        res=self.dfs(s1)
        if s2 in res:
            return True
        else:
            return False

    def dfs(self,s):
        if len(s)==1:
            return [s]
        res=[]
        for i in range(len(s)-1):
            lres=self.dfs(s[:i+1])
            rres=self.dfs(s[i+1:])
            for s1 in lres:
                for s2 in rres:
                    res.append(s1+s2)
                    res.append(s2+s1)
        return  res

