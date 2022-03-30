class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[[0 for _ in range(len(nums))] for _ in range(len(nums))]
        if len(nums)==0:
            return 0

        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if j + i >=len(nums):
                    continue
                for k in range(j,j+i+1):
                    r=1 if j+i+1>=len(nums) else nums[j+i+1]
                    l=1 if j-1<0 else nums[j-1]
                    ldp=0 if k-1<j else dp[j][k-1]
                    rdp=0 if k+1>j+i else dp[k+1][j+i]
                    # print(i,j,k,d)
                    dp[j][j+i]=max(dp[j][j+i],ldp+rdp+l*r*nums[k])
                    print(j, j+i, k, dp[i][j],l,r,ldp,rdp)
        print(dp)
        return dp[0][-1]

a=Solution()
t=[3, 1, 5, 8]
print(a.maxCoins(t))


""""
[[3, 30, 159, 167], [0, 15, 135, 159], [0, 0, 40, 48], [0, 0, 0, 40]]
[[3, 18, 58, 98], [0, 15, 55, 95], [0, 0, 40, 80], [0, 0, 0, 40]]
98
"""
