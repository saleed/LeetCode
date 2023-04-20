class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            dp[i]=dp[i-1]+1 if nums[i]>nums[i-1] else 1

        return max(dp)