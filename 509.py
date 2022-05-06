class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n<=2:
            return 1


        a=1
        b=1
        for i in range(3,n+1):
            tmp=b
            b=a+b
            a=tmp
        return b
