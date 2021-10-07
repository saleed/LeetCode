class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                dp[i]=nums[i]
            else:
                dp[i]=max(nums[i],dp[i-1]+nums[i])
        return max(dp)

    