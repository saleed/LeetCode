class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        p=num
        while p>=10:
            sum=0
            while p:
                sum+=p%10
                p/=10
            p=sum
        return p


