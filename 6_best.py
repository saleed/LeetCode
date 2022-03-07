class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        res=["" for _ in range(numRows)]

        i=0
        flag=-1
        for c in s:
            res[i]+=c
            if i == 0 or i == numRows - 1:
               flag=-1*flag
            i=i+flag
        return "".join(res)







