# def jump(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     G=[[-1 for i in range(len(nums))] for j in range(len(nums))]
#     for i in range(len(nums)):
#         if i-nums[i]>=0:
#             G[i][i-nums[i]]=1
#             G[i-nums[i]][i]=1
#         elif i+nums[i]<=len(nums):
#             G[i][i+nums[i]]=1
#             G[i + nums[i]][i] = 1
#
#
# #how to use queue in python




#有很多种解法！！动态规划略慢，贪心最快！！！
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=self.dp(nums)
        return dp[-1]


    def dp(self,nums):
        dp=[float("inf") for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i-j)<=nums[i]:
                    dp[i]=min(dp[i],dp[j]+1)
        return dp

nums=[2, 3, 1, 1, 4]

a=Solution()
print(a.jump(nums))










