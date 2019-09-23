class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        sel =[ i for i in range(1,n+1)]
        print(sel)

        i=1
        res=""
        k=k-1  ##这里一定是要-1
        while i<=n:
            num=self.fac(n-i)
            # print(k,num)
            res+=str(sel[int(k/num)])
            sel.remove(sel[int(k/num)])
            k=k%num
            i+=1
        return res


    def fac(self,n):
        res=1
        for i in range(1,n+1):
            res*=i
        return res

