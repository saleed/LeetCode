class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=1
        while i*i<=x:
            i+=1
        return i-1
