class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        dp=[0 for _ in range(target+1)]
        dp[0]=1
        for i in range(target+1):
            for num in nums:
                if i-num>=0:
                    dp[i] += dp[i - num]
        return dp[-1]







s=Solution()
nums=[1,2,3]
target=4
print(s.combinationSum4(nums,target))