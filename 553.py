class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        dp=[[[0.0,float("inf"),"",""]for _ in range(len(nums))] for _ in range(len(nums))]
        for l in range(len(nums)):
            for i in range(len(nums)):
                if l==0:
                    dp[i][i+l]=nums[i]

                else:
                    if i+l<len(nums):
                        for j in range(i,i+l):
                            if dp[j+1][i+l][2]!=0:
                                dp[i][i+l][0]=max(float(dp[i][j][3]/dp[j+1][i+l][2]),dp[i][i+l])
                            if  dp[j + 1][i + l]!=0:
                                dp[i][i + l] = min(float(dp[i][j][2] / dp[j + 1][i + l][3]), dp[i][i + l])
        for i in range(len(dpmax)):
            print(dpmax[i])
            print(dpmin[i])
        return dpmax[0][-1]

test=[1000,100,10,2]
ss=Solution()
print(ss.optimalDivision(test))