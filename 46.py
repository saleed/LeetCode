class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res=[]
        self.recursivepmt(nums,0,res)
        print(res)






    def recursivepmt(self,nums,id,res):
        if id==len(nums):
            res.append(nums[:])
            return
        for i in range(id,len(nums)):
            nums[i],nums[id]=nums[id],nums[i]
            self.recursivepmt(nums,id+1,res)
            nums[i],nums[id]=nums[id],nums[i] #####注意要交换回来
        return


nums=[1,2,3]
a=Solution()
print(a.permute(nums))




