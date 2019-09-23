class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        p=1
        while p**2<num:
            p+=1
        if p**2==num:
            return True
        else:
            return False