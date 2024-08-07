class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxl=max(nums)
        dp=(maxl+1)*[0]
        values=(maxl+1)*[0]
        for v in nums:
            values[v]+=v
        dp[0]=values[0]
        dp[1]=max(values[0],values[1])
        for i in range(2,len(dp)):
            dp[i]=max(dp[i-1],dp[i-2]+values[i])
        return dp[-1]
