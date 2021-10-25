class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minvalue=float("inf")
        maxbenefit=-float("inf")
        for v in prices:
            if v<minvalue:
                minvalue=v
            maxbenefit=max(maxbenefit,v-minvalue)
        return maxbenefit
