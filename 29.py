class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:
            return 0
        if dividend==0:
            return 0
        flag=1
        if divisor*dividend<0:
            flag=-1

        divisor=abs(divisor)
        dividend=abs(dividend)

        i=0
        while i*divisor<dividend:
            i+=1

        return flag*(i-1)



