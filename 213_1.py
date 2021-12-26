class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=nums[1]
        for i in range(2,len(nums)):
            for j in range(0,i-1):
                dp[i]=max(nums[i]+dp[i-2],dp[i])
        max1=max(dp[:-1])
        dp=[0]*len(nums)
        dp[0]=0
        dp[1]=nums[1]
        for i in range(2,len(nums)):
            for j in range(0,i-1):
                dp[i]=max(nums[i]+dp[i-2],dp[i])

        max2=max(dp)
        return max(max1,max2)



