class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        p=num
        while p%4==0:
            p=p/4
        return p==1
