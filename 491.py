class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp=[]
        self.dfs(nums,0,tmp)
        res=[]
        for v in tmp:
            if len(v)>1 and v not in res:
                res.append(v)
        return res



    def dfs(self,nums,i,res):
        if i==len(nums):
            return
        tmplen=len(res)
        for j in range(tmplen):
            if nums[i]>=res[j][-1]:
                res.append(res[j]+nums[i])
        res.append([nums[i]])


        self.dfs(nums,i+1,res)