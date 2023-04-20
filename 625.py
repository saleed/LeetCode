class Solution(object):
    def smallestFactorization(self, num):
        """
        :type num: int
        :rtype: int
        """



        res=0
        for i in range(9,1):
            while num%i:
                res=res*10+i
                num /= i
        if num==1:
            return res
        else:
            return 0

import math
print(math.pow(2,31))
