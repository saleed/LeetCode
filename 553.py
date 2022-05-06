class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        dp=[[[float("inf"),0,"",""]for _ in range(len(nums))] for _ in range(len(nums))]
        for l in range(len(nums)):
            for i in range(len(nums)):
                if l==0:
                    dp[i][i+l][0]=float(nums[i])
                    dp[i][i + l][1] = float(nums[i])
                    dp[i][i + l][2] = str(nums[i])
                    dp[i][i + l][3] = str(nums[i])
                else:
                    if i+l<len(nums):
                        for j in range(i,i+l):
                            if dp[j+1][i+l][0]!=0 and dp[i][i+l][1]<float(dp[i][j][1]/dp[j+1][i+l][0]):
                                dp[i][i+l][1]=float(dp[i][j][1]/dp[j+1][i+l][0])
                                if i + l - j > 1:
                                    dp[i][i + l][3] = dp[i][j][3] + "/" + "(" + dp[j + 1][i + l][2] + ")"

                                else:
                                    dp[i][i + l][3] = dp[i][j][3] + "/" + dp[j + 1][i + l][2]

                            if  dp[j + 1][i + l][1]!=0 and dp[i][i +l][0]>float(dp[i][j][0] / dp[j + 1][i + l][1]):
                                dp[i][i +l][0] = float(dp[i][j][0] / dp[j + 1][i + l][1])
                                if i + l - j > 1:
                                    dp[i][i + l][2] = dp[i][j][2] + "/" + "(" + dp[j + 1][i + l][3] + ")"
                                else:
                                    dp[i][i + l][2] = dp[i][j][2] + "/" + dp[j + 1][i + l][3]


        #
        # for i in range(len(dp)):
        #     print(dp[i])

        return dp[0][-1][3]

test=[2,3,4]
ss=Solution()
print(ss.optimalDivision(test))