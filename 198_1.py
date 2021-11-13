class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=nums[1]
        for i in range(2,len(nums)):
            maxv=-float("inf")
            for j in range(i-1):
                maxv=max(maxv,dp[j])
            dp[i]=maxv+nums[i]
        return dp[-1]