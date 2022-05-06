class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        a=a^b
        carry=(a&b)<<1
        while carry>0:
            a=a^carry
            carry=(a&carry)<<1
        return a
