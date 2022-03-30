class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dp=[[0,0] for _ in range(len(nums))]


        if nums[0]>0:
            dp[0][0]=nums[0]
        else:
            dp[0][1]=nums[0]


        maxv=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==0:
                maxv = max(maxv, 0)
                continue
            elif nums[i]>0:
                dp[i][0]=max(nums[i],nums[i]*dp[i-1][0])
                dp[i][1]=min(0,nums[i]*dp[i-1][1])
            else:
                dp[i][0] = max(0, nums[i] * dp[i-1][1])
                dp[i][1] = min(nums[i], nums[i] * dp[i-1][0])
            if dp[i][0]>0:
                maxv=max(maxv,dp[i][0])
            if dp[i][1]<0:
                maxv = max(maxv, dp[i][1])
        return maxv

