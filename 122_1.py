class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxbenefit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxbenefit+=prices[i]-prices[i-1]
        return maxbenefit