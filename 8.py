class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res=int(str)
        if res > pow(2, 31) - 1 or res < -pow(2, 31):
            return 0
        return res