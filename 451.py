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

        dsort=sorted(sdict.items(),key=lambda x:x[1],reverse=True)
        res=""
        for k in dsort:
            res+=k*dsort[k]
        return res