class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        left=n
        res=""
        while left-1>0:
            res+=chr(ord('A')+int((left-1)/26))
            left=le


