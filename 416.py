class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if sum(nums)%2:
            return False
        return self.dp(nums,sum(nums)//2)





    #超时
    def dfs(self,nums,target,cur,id):

        if cur==target:
            return True
        if id<len(nums) and cur<target:
            return self.dfs(nums,target,cur+nums[id],id+1) or self.dfs(nums,target,cur,id+1)
        return False

    #dp


    #0-1背包问题？？？
    #dp[i][j]表示前i个数之和为j
    def dp(self,nums,target):
        dp=[[False for _ in range(target+1)] for _ in range(len(nums))]

        dp[0][0]=False
        for i in range(len(nums)):
            for j in range(target+1):
                if j==0:
                    dp[i][j]=False
                elif i==0:
                    dp[i][j]=True if j==nums[0] else 0
                else:
                    dp[i][j]=dp[i-1][j] or (dp[i-1][j-nums[i]] if j-nums[i]>0 else False)

        return dp[len(nums)-1][target]









a=Solution()
print(a.canPartition([1,5,11,5]))
