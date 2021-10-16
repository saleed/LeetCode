class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(0,nums,res,[])
        return res

    def dfs(self,i,nums,res,cur):
        if i==len(nums):
            res.append(cur[:])
            return
        self.dfs(i+1,nums,res,cur)
        cur.append(nums[i])
        self.dfs(i+1,nums,res,cur)
        cur.pop()