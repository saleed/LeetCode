
import  math

math.factorial()

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n>=10: ###错误的结论
            return 9*math.factorial(9)
        res=[0]*10
        res[0]=1
        for i in range(1,10):
            res[i]=res[i-1]+9*math.factorial(9)/math.factorial(10-i)
        return res[n]
