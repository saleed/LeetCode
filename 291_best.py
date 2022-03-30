class Solution(object):
    def wordPatternMatch(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pdict={}
        sdict={}

        return self.dfs(pattern,s,pdict,sdict)

    def dfs(self,pattern,s,pdict,sdict):
        if pattern=="" and s=="":
            return True
        if len(pattern)>0 and len(s)>0:
            tmpch=pattern[0]
            flag=False
            for i in range(len(s)):
                if tmpch not in pdict and s[:i+1] not in sdict:
                    pdict[tmpch]=s[:i+1]
                    sdict[s[:i+1]]=tmpch
                    if self.dfs(pattern[1:], s[i + 1:], pdict, sdict):
                        return True
                    del pdict[tmpch]
                    del sdict[s[:i + 1]]

                elif tmpch in pdict and s[:i+1] in sdict and pdict[tmpch]==s[:i+1] and sdict[s[:i+1]]==tmpch:
                    if self.dfs(pattern[1:],s[i+1:],pdict,sdict):
                        return True
                else:
                    continue
            return False

        return False





