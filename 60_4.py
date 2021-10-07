class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res=""
        select=""
        for i in range(1,n+1):
            select+=str(i)

        ####一定要注意二进制的实际含义：比如1%2=1 1/2等于0 表示第0个循环，第2个数     3%2=1，3/2=1 表示第1个循环第二个数，！！！！！！
        k=k-1
        for i in range(n):
            fac=self.fac(n-i-1)
            id=k/fac
            res+=select[id]
            k=k%fac
            select=select[:id]+select[id+1:]
        return res



    def fac(self,i):
        res=1
        for j in range(1,i+1):
            res*=j
        return res


if __name__=="__main__":
    a=Solution()
    print(a.getPermutation(4,9))





