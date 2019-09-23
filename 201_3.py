class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res=0
        for i in range(1,32):
            div=pow(2,i)
            flag=0
            if int(m/div)==int(n/div) and m%div>=pow(2,i-1):
                flag=1
            res+=pow(2,i-1)*flag

        return res





a=Solution()
test=[5,7]


print(a.rangeBitwiseAnd(5,7))
print(a.rangeBitwiseAnd(0,1))
