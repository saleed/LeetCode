class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])

        dp=[0]*len(nums)

        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])

        for j in range(2,len(nums)):
            dp[j]=max(dp[j-1],dp[j-2]+nums[j])
        return dp[-1]