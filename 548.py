class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        limit=20
        target=int(sum(nums)/2)
        print(target)
        dp=[[0 for _ in range(limit)] for _ in range(len(nums))]
        dp[0][0]=True
        for i in range(len(nums)):
            if i==0:
                dp[i][nums[0]]=True
                continue
            for j in range(limit):
                if dp[i-1][j] or (j-nums[i]>=0 and dp[i-1][j-nums[i]]):
                    dp[i][j]=True
            print(dp[i])
        return dp[-1][target]

test=[1,2,1,2,1,2,1,2]
ss=Solution()
print(ss.splitArray(test))