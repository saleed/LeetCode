class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """


        sdict={}
        for v in s:
            if v in sdict:
                sdict[v]+=1
            else:
                sdict[v]=1
        print(sdict.items())
        dsort=sorted(sdict.items(),key=lambda x:x[1],reverse=True) ###学会使用items
        print(dsort)
        res=""
        for k in dsort:
            res+=k[0]*k[1]
        return res

a=Solution()
s = "tree"
print(a.frequencySort(s))