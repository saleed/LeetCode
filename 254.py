import math

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        sqrtn=math.sqrt(n)

        res=[]
        fo