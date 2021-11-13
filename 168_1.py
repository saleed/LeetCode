class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res=""
        columnNumber=columnNumber-1
        while columnNumber>=0:
            left=columnNumber%26
            res+=chr(left+ord("A"))
            columnNumber=columnNumber/26-1
        return res


a=Solution()
print(a.convertToTitle(1))