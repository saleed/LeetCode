##################################对余数和取模操作理解不够深刻


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        sel=[]
        for i in range(1,n+1):
            sel.append(str(i))
        res=""
        k=k-1
        for i in list(reversed(range(n))):
            div=int(k/self.fac(i))
            k=k%self.fac(i)
            res+=sel[div]
            sel.remove(sel[div])
        return res



    def fac(self,n):
        res=1
        for i in range(1,n+1):
            res*=i
        return res

a=Solution()
print(a.getPermutation(3,6))

