class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res=[]
        self.dfs(0,nums,target,[],res)
        return res





    def dfs(self,i,nums,target,tmp,res):
        if len(res)==3:
            res.append(tmp[:])
        else:
            tmpsum=sum(res)
            if i>=len(nums):
                return
            self.dfs(i+1,nums,target,tmp,res)
            if tmpsum+nums[i]<target:
                tmp.append(nums[i])
                self.dfs(i+1,nums,target,tmp,res)
                tmp.pop()



