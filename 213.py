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
            return max(nums[0],nums[1])
        dp=[0]*len(nums)
        #case1:
        dp[0]=0
        dp[1]=nums[1]
        self.robdp(dp,nums)
        case1=dp[len(nums)-1]
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        self.robdp(dp,nums)
        case2=dp[len(nums)-2]
        return max(case1,case2)

    def robdp(self,dp,nums):
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])







test=[0]*5
print test
test[0]=1
print test

