class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=""
        while num:
            res=str(num%7)+res
            num/=7
        return res