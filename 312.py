class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i]=nums[i]
        for i in range(len(nums)):
            for j in range(i+1):
                for k in list(reversed(range(j,i+1))):
                    left=0
                    right=0
                    if k!=j:
                        left=dp[j][k-1]
                    if k!=i:
                        right=dp[k+1][i]
                    dp[j][i]=max(dp[j][i],left+right+self.getnumval(nums,j,i,k))
                    print j,i,k,self.getnumval(nums,j,i,k),left,right,dp[j][i]

        print dp
    def getnumval(self,nums,i,j,k):
        if i<0 or i>len(nums):
            return -1
        left=1
        right=1
        if k==i:
            left=1
        else:
            left=nums[k-1]
        if k==j:
            right=1
        else:
            right=nums[k+1]
        return nums[k]*left*right


nums=[3,1,5,8]
a=Solution()
a.maxCoins(nums)
