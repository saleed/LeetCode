class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dp=[1]*len(nums)
        dp[0]=1
        pre=[0]*len(nums)
        for i in range(len(nums)):
            pre[i]=i
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j] and dp[i]<dp[j]+1:
                    pre[i]=j  #back tracking
                    dp[i]=dp[j]+1
        id=0
        # print dp
        maxv=-float("inf")
        for i in range(len(dp)):
            if dp[i]>maxv:
                maxv=dp[i]
                id=i
        return maxv
        #back-tracking
        # res=[]
        # while pre[id]!=id:  ###back-tracking
        #     res.append(nums[id])
        #     id=pre[id]
        # return list(reversed(res))

test=[10,9,2,5,3,7,101,18]
a=Solution()
print a.lengthOfLIS(test)


