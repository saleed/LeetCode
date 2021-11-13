class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp=[[-float("inf"),float("inf")] for _ in range(len(nums)+1)]*len(nums)
        if nums==None:
            return 0
        for i in range(1,len(nums)):
            if nums[i-1]==0:
                dp[i]=[0,0,False]
            else:
                if nums[i-1]>0:
                    if dp[i-1][0]==0:
                        upzero=nums[i-1]
                    else:
                        upzero=nums[i-1]*dp[i-1][0]
                    downzero=0
                    if dp[i-1][1]!=0:
                     downzero= nums[i - 1] * dp[i - 1][1]
                    dp[i]=[upzero,downzero]
                else:
                    upzero=0
                    if dp[i-1][1]!=0:
                        upzero=dp[i-1][1]*nums[i-1]

                    if dp[i-1][0]!=0:
                        downzero=dp[i-1][0]*nums[i-1]
                    else:
                        downzero=nums[i-1]

                    dp[i] = [upzero, downzero]

        maxv=-float("inf")
        for v in dp:
            maxv=max(maxv,v[0])
        return maxv




