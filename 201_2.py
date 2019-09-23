class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res=0
        for i in range(1,32+1):
            if self.rangeIsOneOfBit(m,n,i):
                print(self.rangeIsOneOfBit(m,n,i))
                res+=pow(2,i-1)
        return res




    def rangeIsOneOfBit(self,m,n,bit):
        div=pow(2,bit)

        # print(m % div)
        # print(n%div)
        return int(n/div)==int(m/div) and m%div>=int(div/2) and n%div<div

a=Solution()
test=[5,7]

101
110
111

print(a.rangeBitwiseAnd(5,7))
