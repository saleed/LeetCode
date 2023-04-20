class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp=[1]*len(nums)
        maxl=1
        cnt=0

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
                    if dp[i]>maxl:
                        maxl=dp[i]
                        cnt=1
                    elif dp[i]==maxl:
                        cnt+=1
            if maxl==1:
                cnt+=1





        return cnt