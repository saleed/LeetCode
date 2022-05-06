class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        row=0 ##
        tmp=0
        while tmp<=n:
            row+=1
            tmp+=row
        return row-1

