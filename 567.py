class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1=sorted(s1)
        # perm=self.permutation(s1)
        for i in range(len(s2)):
            if i+len(s1)<=len(s2) and sorted(s2[i:i+len(s1)])==s1:
                return True
        return False



    def permutation(self,s):
        res=[]
        vis=set()
        for i in range(len(s)):
            if s[i] in vis:
                continue
            vis.add(s[i])
            news=s[:i]+s[i+1:]
            newres=self.permutation(news)
            if len(newres)>0:
                for v in newres:
                    tmp=s[i]+v
                    res.append(tmp)
            else:
                res.append(s[i])
        return res



s="dinitrophenylhydrazine"
ss=Solution()
print(ss.permutation(s))





















test="1245241"
print(set(test))
