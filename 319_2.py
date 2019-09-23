class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        #其实就是计算1~n中每个数因子的个数，如果个数为偶数，终态为关闭，否则为打开
        #此种方法仍然超时
        ele=[0]*(n+1)
        for i in range(1,n+1):
            p=1
            while p*i<=n:
                ele[p*i]+=1
                p+=1
        count=0
        for i in ele[1:]:
            if i%2:
                count+=1
        return count

a=Solution()
print(a.bulbSwitch(3))
