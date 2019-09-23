class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(0,nums,[],res)
        return res


    def dfs(self,id,nums,cur,res):
        if id==len(nums):
            res.append(cur[:])
            return
        self.dfs(id+1,nums,cur,res)
        cur.append(nums[id])
        self.dfs(id+1,nums,cur,res)
        cur.pop()
