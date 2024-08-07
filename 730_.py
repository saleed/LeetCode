class Solution(object):
    def countPalindromicSubsequences(self, s):
        """
        :type s: str
        :rtype: int小
        """
        res=0
        sdict={}
        for v in s:
            if v in sdict:
                sdict[v]+=1
            else:
                sdict[v]=1

        res+=self.cal(sdict)
        for k in sdict:
            sdict[k]-=1
            res+=self.cal(sdict)
            sdict[k]+=1
        return res


    def fac(self,n):
        res=1
        for i in range(1,n+1):
            res*=i
        return  res

    def cal(self,sdict):
        sumv = 0
        div = 1
        for k1 in sdict:
            sumv += sdict[k1] / 2
            if sdict[k1] / 2 > 0:
                div *= self.fac(sdict[k1] / 2)
        return self.fac(sumv)/div
