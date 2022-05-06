class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()
        cnt=0
        for i in range(len(g)):
            for j in range(len(s))[::-1]:
                if s[j] <=g[i]:
                    s[i]=-1
                    cnt+=1
        return cnt