class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res=[]
        self.dfs(nums,target,[],res)
        return res





    def dfs(self,nums,left,cur,res):
        if left==0:
            res.append(cur[:])
            return
        if left>0:
            for i in range(len(nums)):
                    cur.append(nums[i])
                    self.dfs(nums,left-nums[i],cur,res)
                    cur.pop()
        return


a=Solution()
print(a.combinationSum4([1,2,3],4))