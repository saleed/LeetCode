class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        for itv in range(len(nums)):
            for j in range(len(nums)):
                if j + itv >= len(nums):
                    continue
                for k in range(j, j + itv + 1):
                    right=1 if j+itv+1>=len(nums) else nums[j+itv+1]
                    left=1 if j-1<0 else nums[j-1]
                    ldp=dp[j][k-1] if k-1>=0 else 0
                    rdp=dp[k+1][j+itv] if k+1<len(nums) else 0
                    dp[j][j + itv] = max(left * right * nums[k] +rdp+ldp, dp[j][j + itv])
        print(dp)
        return dp[0][-1]


a=Solution()
t=[3, 1, 5, 8]
print(a.maxCoins(t))