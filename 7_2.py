class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>pow(2,31)-1 or x<-pow(2,31):
            return 0
        flag=1
        if x<0:
            flag=-1
            x=-x
        res=0
        while x:
            res=res*10+x%10
            x/=10
        if res*flag>pow(2,31)-1 or res*flag<-pow(2,31):
            return 0
        return res*flag

a=Solution()
x=1534236469
print(a.reverse(x))
