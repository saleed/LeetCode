class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res=[]
        self.recursive(nums,0,res)
        return res

    def recursive(self,nums,i,res):
        if i>=len(nums):
            res.append(nums[:])
            return

        for j in range(i,len(nums)):
            nums[i],nums[j]=nums[j],nums[i]
            self.recursive(nums,i+1,res)
            nums[j],nums[i]=nums[i],nums[j]
