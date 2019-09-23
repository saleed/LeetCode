class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if p <= 0:
            return False
        p = num
        while p % 5 == 0:
            p /= 5
        while p % 2 == 0:
            p /= 2
        while p % 3 == 0:
            p /= 3
        if p != 1:
            return False
        else:
            return True
