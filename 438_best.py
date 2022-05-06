class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        pdict={}
        for v in p:
            if v in pdict:
                pdict[v]+=1
            else:
                pdict[v]=1
        sdict={}
        res=[]
        for i in range(len(s)):

            if i>=len(p):
                sdict[s[i-len(p)]]-=1
                if sdict[s[i-len(p)]]==0:
                    del sdict[s[i-len(p)]]
            if s[i] in sdict:
                sdict[s[i]] += 1
            else:
                sdict[s[i]] = 1
            if pdict == sdict:
                res.append(i - len(p)+1)
        return res

s="cbaebabacd"
p="abc"
ss=Solution()
print(ss.findAnagrams(s,p))