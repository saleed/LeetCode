class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # res=[0]
        # self.dfs(nums,0,target,0,res)
        # return res[0]
        return self.dpSolve(nums,target)


    def dfs(self,nums,i,target,tmp,res):
        if i==len(nums) and tmp==target:
            res[0]+=1
            return
        elif i<len(nums):
            self.dfs(nums,i+1,target,tmp+nums[i],res)
            self.dfs(nums,i+1,target,tmp-nums[i],res)



    def dpSolve(self,nums,target):
        maxsum=0
        for v in nums:
            if v>0:
                maxsum+=v
            else:
                maxsum+=(-v)
        if target>maxsum or target<-maxsum:
            return 0
        dp=[[0 for _ in range(maxsum*2+1)] for _ in range(len(nums))]



        for i in range(len(nums)):
            if i==0:
                dp[i][nums[i] + maxsum] += 1
                dp[i][-nums[i] + maxsum] += 1
                print(dp[i])
                continue
            for j in range(maxsum*2+1):
                if j-nums[i]>=0 and j-nums[i]<maxsum*2+1 and dp[i-1][j-nums[i]]>0:
                    dp[i][j]+=dp[i-1][j-nums[i]]
                if j+nums[i]>=0 and j+nums[i]<maxsum*2+1 and dp[i-1][j+nums[i]]>0:
                    dp[i][j]+=dp[i-1][j+nums[i]]
            print(dp[i])
        return dp[-1][target+maxsum]




ss=Solution()

nums = [0,0,0,0,0,0,0,0,1]

target = 1
print(ss.findTargetSumWays(nums,target))



