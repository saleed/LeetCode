class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: Lit[int]
        :rtype: bool
        """




        dp=[[ 0 for _ in range(len(nums))] for _ in range(len(nums))]
        sumn=[[0 for _  in range(len(nums))] for _ in range(len(nums))]
        for l in range(len(nums)):
            for j in range(len(nums)):
                if l==0:
                    sumn[j][j+l]=nums[j]
                elif j+l<len(nums):
                    sumn[j][j+l]=nums[j+l]+sumn[j][j+l-1]



        for l in range(len(nums)):
            for j in range(len(nums)):
                if l==0:
                    dp[j][j]=nums[j]
                elif j+l<len(nums):
                    dp[j][j+l]=max((sumn[j][j+l-1]-dp[j][j+l-1])+nums[j+l],(sumn[j+1][j+l]-dp[j+1][j+l])+nums[j])

        return dp[0][-1]>=sumn[0][-1]-dp[0][-1]
