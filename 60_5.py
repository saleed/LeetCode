class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        l=[i for i in range(1,n+1)]
        res=""
        for i in range(1,n+1):
            print(k,self.fac(n-i),l)
            fac=self.fac(n-i)
            res+=str(l[(k-1)/fac])
            l.remove(l[(k-1)/fac])
            k=(k-1)%fac+1

        return res

    def fac(self,i):
        res=1
        for j in range(1,i+1):
            res*=j
        return res




if __name__=="__main__":
    a=Solution()
    print(a.getPermutation(4,9))

