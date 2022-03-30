class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        sel=[]
        for i in range(1,n+1):
            sel.append(i)
        k=k-1
        res=""
        while len(sel)>0:
            num=self.fac(len(sel)-1)
            div=k/num
            k=k%num
            res+=str(sel[div])
            sel.remove(sel[div])
        return res

    def fac(self,n):
        res=1
        for i in range(1,n+1):
            res*=i
        return res

test=[1,2,3,4]
a=Solution()
print(a.getPermutation(4,9))