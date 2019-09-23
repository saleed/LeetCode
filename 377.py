class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 0

        return self.DPSolve(nums,target)



        left=target
        nums.sort()
        res=[]
        self.dfs(nums,left,res,[])
        return len(res)



    def dfs(self,nums,left,res,cursel):
        print left,cursel
        if left==0:
            res.append(cursel[:])
            return
        for i in nums:
            if i>left:
                break
            else:
                cursel.append(i)
                self.dfs(nums,left-i,res,cursel)
                cursel.pop()
        return
    def DPSolve(self,nums,target):
        dp=[0]*(target+1)
        dp[0]=1
        #nums is a array with positive integer
        for i in range(target+1):
            for j in nums:
                if i-j>=0:
                    dp[i]+=dp[i-j]
        print dp
        return dp[target]


a=Solution()
In= [1, 2, 3]
print a.combinationSum4(In,4)

In=[4,2,1]
target=32
print a.combinationSum4(In,target)