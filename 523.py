class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        #####连续子数组！！！！！

        presum=[0]*len(nums)
        vdict={0:-1} ##### notice this
        prev=0
        for i in range(0,len(nums)):
            presum[i]=prev+nums[i]

            left=presum[i]%k
            if  left in vdict:
                if i-vdict[left]>=2:
                    return True

            else:   ####left not in vdict add !!!!!!!will not update if left
                vdict[left]=i
            prev=presum[i]
        return False



        # sumv=sum(nums)
        # dp=[[0 for _ in range(sumv+1)] for _ in range(len(nums))]
        #
        # for i in range(len(nums)):
        #     for j in range(sumv+1):
        #         if i==0:
        #             dp[i][j]=1 if j==nums[i] else 0
        #         else:
        #             dp[i][j]=dp[i-1][j]
        #             if nums[i]==j:
        #                 dp[i][j]=max(1,dp[i][j])
        #             if j-nums[i]>=0 and  dp[i-1][j-nums[i]]>0:
        #                 dp[i][j]=max(dp[i][j],dp[i-1][j-nums[i]]+1)
        # for v in dp:
        #     print(v)
        # return True if dp[-1][k]>=2 else False


ss=Solution()
test=[23,2,4,6,7]
k=6
ss.checkSubarraySum(test,k)