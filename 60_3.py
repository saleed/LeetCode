class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        sel =[ i for i in range(1,n+1)]
        res=""

        if k>self.fac(n):
            return ""



        ####一定要注意二进制的实际含义：比如1%2=1 1/2等于0 表示第0个循环，第2个数     3%2=1，3/2=1 表示第1个循环第二个数
        k=k-1
        while n>0:
            # print(k)
            bit=(k//self.fac(n-1))
            print(bit)
            res+=str(sel[bit])
            sel.remove(sel[bit])
            k=k%self.fac(n-1)
            n-=1

        return res


    def fac(self,n):
        res=1
        for i in range(1,n+1):
            res*=i
        return res



a=Solution()
print(a.getPermutation(3,3))
print(a.fac(3))

# 123
# 132
# 213
# 231
# 312
# 321
