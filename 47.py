class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res=[]
        nums.sort()
        self.recursivepmt(nums,0,res)
        # print(res,len(res))
        return res




思路1:

# #重复出现的原因：交换过程中，重复使用了选过的数字与数组首数交换：
如果不使用集合，先对数组排序，然后按照下面原则：
#     1.跳过于数组首数相同的数
#     2.对于重复的数直接跳过
上述想法是错误的，因为排列生成过程中，会打乱已有顺序

直接使用集合记录之前已经选择过的数字

    def recursivepmt(self,nums,id,res):
        if id==len(nums):
            res.append(nums[:])
            return
        pre=float("inf")
        # self.recursivepmt(nums, id + 1, res)
        sel=set()
        for i in range(id,len(nums)):
            if nums[i] in sel:
                continue
            sel.add(nums[i])
            nums[i],nums[id]=nums[id],nums[i]
            self.recursivepmt(nums, id + 1, res)
            nums[i],nums[id]=nums[id],nums[i] #####注意要交换回来
        return


nums=[1,2,2,3]
a=Solution()
print(a.permuteUnique(nums))

nums=[3,3,0,3]
print(a.permuteUnique(nums))


nums=[0,1,0,0,9]
print(a.permuteUnique(nums))

asw=[[0,0,0,1,9],[0,0,0,9,1],[0,0,1,0,9],[0,0,1,9,0],[0,0,9,0,1],[0,0,9,1,0],[0,1,0,0,9],[0,1,0,9,0],[0,1,9,0,0],[0,9,0,0,1],[0,9,0,1,0],[0,9,1,0,0],[1,0,0,0,9],[1,0,0,9,0],[1,0,9,0,0],[1,9,0,0,0],[9,0,0,0,1],[9,0,0,1,0],[9,0,1,0,0],[9,1,0,0,0]]
print(asw)

nums=[-1,2,0,-1,1,0,1]
print(a.permuteUnique(nums))
aws=[[-1,-1,0,0,1,1,2],[-1,-1,0,0,1,2,1],[-1,-1,0,0,2,1,1],[-1,-1,0,1,0,1,2],[-1,-1,0,1,0,2,1],[-1,-1,0,1,1,0,2],[-1,-1,0,1,1,2,0],[-1,-1,0,1,2,0,1],[-1,-1,0,1,2,1,0],[-1,-1,0,2,0,1,1],[-1,-1,0,2,1,0,1],[-1,-1,0,2,1,1,0],[-1,-1,1,0,0,1,2],[-1,-1,1,0,0,2,1],[-1,-1,1,0,1,0,2],[-1,-1,1,0,1,2,0],[-1,-1,1,0,2,0,1],[-1,-1,1,0,2,1,0],[-1,-1,1,1,0,0,2],[-1,-1,1,1,0,2,0],[-1,-1,1,1,2,0,0],[-1,-1,1,2,0,0,1],[-1,-1,1,2,0,1,0],[-1,-1,1,2,1,0,0],[-1,-1,2,0,0,1,1],[-1,-1,2,0,1,0,1],[-1,-1,2,0,1,1,0],[-1,-1,2,1,0,0,1],[-1,-1,2,1,0,1,0],[-1,-1,2,1,1,0,0],[-1,0,-1,0,1,1,2],[-1,0,-1,0,1,2,1],[-1,0,-1,0,2,1,1],[-1,0,-1,1,0,1,2],[-1,0,-1,1,0,2,1],[-1,0,-1,1,1,0,2],[-1,0,-1,1,1,2,0],[-1,0,-1,1,2,0,1],[-1,0,-1,1,2,1,0],[-1,0,-1,2,0,1,1],[-1,0,-1,2,1,0,1],[-1,0,-1,2,1,1,0],[-1,0,0,-1,1,1,2],[-1,0,0,-1,1,2,1],[-1,0,0,-1,2,1,1],[-1,0,0,1,-1,1,2],[-1,0,0,1,-1,2,1],[-1,0,0,1,1,-1,2],[-1,0,0,1,1,2,-1],[-1,0,0,1,2,-1,1],[-1,0,0,1,2,1,-1],[-1,0,0,2,-1,1,1],[-1,0,0,2,1,-1,1],[-1,0,0,2,1,1,-1],[-1,0,1,-1,0,1,2],[-1,0,1,-1,0,2,1],[-1,0,1,-1,1,0,2],[-1,0,1,-1,1,2,0],[-1,0,1,-1,2,0,1],[-1,0,1,-1,2,1,0],[-1,0,1,0,-1,1,2],[-1,0,1,0,-1,2,1],[-1,0,1,0,1,-1,2],[-1,0,1,0,1,2,-1],[-1,0,1,0,2,-1,1],[-1,0,1,0,2,1,-1],[-1,0,1,1,-1,0,2],[-1,0,1,1,-1,2,0],[-1,0,1,1,0,-1,2],[-1,0,1,1,0,2,-1],[-1,0,1,1,2,-1,0],[-1,0,1,1,2,0,-1],[-1,0,1,2,-1,0,1],[-1,0,1,2,-1,1,0],[-1,0,1,2,0,-1,1],[-1,0,1,2,0,1,-1],[-1,0,1,2,1,-1,0],[-1,0,1,2,1,0,-1],[-1,0,2,-1,0,1,1],[-1,0,2,-1,1,0,1],[-1,0,2,-1,1,1,0],[-1,0,2,0,-1,1,1],[-1,0,2,0,1,-1,1],[-1,0,2,0,1,1,-1],[-1,0,2,1,-1,0,1],[-1,0,2,1,-1,1,0],[-1,0,2,1,0,-1,1],[-1,0,2,1,0,1,-1],[-1,0,2,1,1,-1,0],[-1,0,2,1,1,0,-1],[-1,1,-1,0,0,1,2],[-1,1,-1,0,0,2,1],[-1,1,-1,0,1,0,2],[-1,1,-1,0,1,2,0],[-1,1,-1,0,2,0,1],[-1,1,-1,0,2,1,0],[-1,1,-1,1,0,0,2],[-1,1,-1,1,0,2,0],[-1,1,-1,1,2,0,0],[-1,1,-1,2,0,0,1],[-1,1,-1,2,0,1,0],[-1,1,-1,2,1,0,0],[-1,1,0,-1,0,1,2],[-1,1,0,-1,0,2,1],[-1,1,0,-1,1,0,2],[-1,1,0,-1,1,2,0],[-1,1,0,-1,2,0,1],[-1,1,0,-1,2,1,0],[-1,1,0,0,-1,1,2],[-1,1,0,0,-1,2,1],[-1,1,0,0,1,-1,2],[-1,1,0,0,1,2,-1],[-1,1,0,0,2,-1,1],[-1,1,0,0,2,1,-1],[-1,1,0,1,-1,0,2],[-1,1,0,1,-1,2,0],[-1,1,0,1,0,-1,2],[-1,1,0,1,0,2,-1],[-1,1,0,1,2,-1,0],[-1,1,0,1,2,0,-1],[-1,1,0,2,-1,0,1],[-1,1,0,2,-1,1,0],[-1,1,0,2,0,-1,1],[-1,1,0,2,0,1,-1],[-1,1,0,2,1,-1,0],[-1,1,0,2,1,0,-1],[-1,1,1,-1,0,0,2],[-1,1,1,-1,0,2,0],[-1,1,1,-1,2,0,0],[-1,1,1,0,-1,0,2],[-1,1,1,0,-1,2,0],[-1,1,1,0,0,-1,2],[-1,1,1,0,0,2,-1],[-1,1,1,0,2,-1,0],[-1,1,1,0,2,0,-1],[-1,1,1,2,-1,0,0],[-1,1,1,2,0,-1,0],[-1,1,1,2,0,0,-1],[-1,1,2,-1,0,0,1],[-1,1,2,-1,0,1,0],[-1,1,2,-1,1,0,0],[-1,1,2,0,-1,0,1],[-1,1,2,0,-1,1,0],[-1,1,2,0,0,-1,1],[-1,1,2,0,0,1,-1],[-1,1,2,0,1,-1,0],[-1,1,2,0,1,0,-1],[-1,1,2,1,-1,0,0],[-1,1,2,1,0,-1,0],[-1,1,2,1,0,0,-1],[-1,2,-1,0,0,1,1],[-1,2,-1,0,1,0,1],[-1,2,-1,0,1,1,0],[-1,2,-1,1,0,0,1],[-1,2,-1,1,0,1,0],[-1,2,-1,1,1,0,0],[-1,2,0,-1,0,1,1],[-1,2,0,-1,1,0,1],[-1,2,0,-1,1,1,0],[-1,2,0,0,-1,1,1],[-1,2,0,0,1,-1,1],[-1,2,0,0,1,1,-1],[-1,2,0,1,-1,0,1],[-1,2,0,1,-1,1,0],[-1,2,0,1,0,-1,1],[-1,2,0,1,0,1,-1],[-1,2,0,1,1,-1,0],[-1,2,0,1,1,0,-1],[-1,2,1,-1,0,0,1],[-1,2,1,-1,0,1,0],[-1,2,1,-1,1,0,0],[-1,2,1,0,-1,0,1],[-1,2,1,0,-1,1,0],[-1,2,1,0,0,-1,1],[-1,2,1,0,0,1,-1],[-1,2,1,0,1,-1,0],[-1,2,1,0,1,0,-1],[-1,2,1,1,-1,0,0],[-1,2,1,1,0,-1,0],[-1,2,1,1,0,0,-1],[0,-1,-1,0,1,1,2],[0,-1,-1,0,1,2,1],[0,-1,-1,0,2,1,1],[0,-1,-1,1,0,1,2],[0,-1,-1,1,0,2,1],[0,-1,-1,1,1,0,2],[0,-1,-1,1,1,2,0],[0,-1,-1,1,2,0,1],[0,-1,-1,1,2,1,0],[0,-1,-1,2,0,1,1],[0,-1,-1,2,1,0,1],[0,-1,-1,2,1,1,0],[0,-1,0,-1,1,1,2],[0,-1,0,-1,1,2,1],[0,-1,0,-1,2,1,1],[0,-1,0,1,-1,1,2],[0,-1,0,1,-1,2,1],[0,-1,0,1,1,-1,2],[0,-1,0,1,1,2,-1],[0,-1,0,1,2,-1,1],[0,-1,0,1,2,1,-1],[0,-1,0,2,-1,1,1],[0,-1,0,2,1,-1,1],[0,-1,0,2,1,1,-1],[0,-1,1,-1,0,1,2],[0,-1,1,-1,0,2,1],[0,-1,1,-1,1,0,2],[0,-1,1,-1,1,2,0],[0,-1,1,-1,2,0,1],[0,-1,1,-1,2,1,0],[0,-1,1,0,-1,1,2],[0,-1,1,0,-1,2,1],[0,-1,1,0,1,-1,2],[0,-1,1,0,1,2,-1],[0,-1,1,0,2,-1,1],[0,-1,1,0,2,1,-1],[0,-1,1,1,-1,0,2],[0,-1,1,1,-1,2,0],[0,-1,1,1,0,-1,2],[0,-1,1,1,0,2,-1],[0,-1,1,1,2,-1,0],[0,-1,1,1,2,0,-1],[0,-1,1,2,-1,0,1],[0,-1,1,2,-1,1,0],[0,-1,1,2,0,-1,1],[0,-1,1,2,0,1,-1],[0,-1,1,2,1,-1,0],[0,-1,1,2,1,0,-1],[0,-1,2,-1,0,1,1],[0,-1,2,-1,1,0,1],[0,-1,2,-1,1,1,0],[0,-1,2,0,-1,1,1],[0,-1,2,0,1,-1,1],[0,-1,2,0,1,1,-1],[0,-1,2,1,-1,0,1],[0,-1,2,1,-1,1,0],[0,-1,2,1,0,-1,1],[0,-1,2,1,0,1,-1],[0,-1,2,1,1,-1,0],[0,-1,2,1,1,0,-1],[0,0,-1,-1,1,1,2],[0,0,-1,-1,1,2,1],[0,0,-1,-1,2,1,1],[0,0,-1,1,-1,1,2],[0,0,-1,1,-1,2,1],[0,0,-1,1,1,-1,2],[0,0,-1,1,1,2,-1],[0,0,-1,1,2,-1,1],[0,0,-1,1,2,1,-1],[0,0,-1,2,-1,1,1],[0,0,-1,2,1,-1,1],[0,0,-1,2,1,1,-1],[0,0,1,-1,-1,1,2],[0,0,1,-1,-1,2,1],[0,0,1,-1,1,-1,2],[0,0,1,-1,1,2,-1],[0,0,1,-1,2,-1,1],[0,0,1,-1,2,1,-1],[0,0,1,1,-1,-1,2],[0,0,1,1,-1,2,-1],[0,0,1,1,2,-1,-1],[0,0,1,2,-1,-1,1],[0,0,1,2,-1,1,-1],[0,0,1,2,1,-1,-1],[0,0,2,-1,-1,1,1],[0,0,2,-1,1,-1,1],[0,0,2,-1,1,1,-1],[0,0,2,1,-1,-1,1],[0,0,2,1,-1,1,-1],[0,0,2,1,1,-1,-1],[0,1,-1,-1,0,1,2],[0,1,-1,-1,0,2,1],[0,1,-1,-1,1,0,2],[0,1,-1,-1,1,2,0],[0,1,-1,-1,2,0,1],[0,1,-1,-1,2,1,0],[0,1,-1,0,-1,1,2],[0,1,-1,0,-1,2,1],[0,1,-1,0,1,-1,2],[0,1,-1,0,1,2,-1],[0,1,-1,0,2,-1,1],[0,1,-1,0,2,1,-1],[0,1,-1,1,-1,0,2],[0,1,-1,1,-1,2,0],[0,1,-1,1,0,-1,2],[0,1,-1,1,0,2,-1],[0,1,-1,1,2,-1,0],[0,1,-1,1,2,0,-1],[0,1,-1,2,-1,0,1],[0,1,-1,2,-1,1,0],[0,1,-1,2,0,-1,1],[0,1,-1,2,0,1,-1],[0,1,-1,2,1,-1,0],[0,1,-1,2,1,0,-1],[0,1,0,-1,-1,1,2],[0,1,0,-1,-1,2,1],[0,1,0,-1,1,-1,2],[0,1,0,-1,1,2,-1],[0,1,0,-1,2,-1,1],[0,1,0,-1,2,1,-1],[0,1,0,1,-1,-1,2],[0,1,0,1,-1,2,-1],[0,1,0,1,2,-1,-1],[0,1,0,2,-1,-1,1],[0,1,0,2,-1,1,-1],[0,1,0,2,1,-1,-1],[0,1,1,-1,-1,0,2],[0,1,1,-1,-1,2,0],[0,1,1,-1,0,-1,2],[0,1,1,-1,0,2,-1],[0,1,1,-1,2,-1,0],[0,1,1,-1,2,0,-1],[0,1,1,0,-1,-1,2],[0,1,1,0,-1,2,-1],[0,1,1,0,2,-1,-1],[0,1,1,2,-1,-1,0],[0,1,1,2,-1,0,-1],[0,1,1,2,0,-1,-1],[0,1,2,-1,-1,0,1],[0,1,2,-1,-1,1,0],[0,1,2,-1,0,-1,1],[0,1,2,-1,0,1,-1],[0,1,2,-1,1,-1,0],[0,1,2,-1,1,0,-1],[0,1,2,0,-1,-1,1],[0,1,2,0,-1,1,-1],[0,1,2,0,1,-1,-1],[0,1,2,1,-1,-1,0],[0,1,2,1,-1,0,-1],[0,1,2,1,0,-1,-1],[0,2,-1,-1,0,1,1],[0,2,-1,-1,1,0,1],[0,2,-1,-1,1,1,0],[0,2,-1,0,-1,1,1],[0,2,-1,0,1,-1,1],[0,2,-1,0,1,1,-1],[0,2,-1,1,-1,0,1],[0,2,-1,1,-1,1,0],[0,2,-1,1,0,-1,1],[0,2,-1,1,0,1,-1],[0,2,-1,1,1,-1,0],[0,2,-1,1,1,0,-1],[0,2,0,-1,-1,1,1],[0,2,0,-1,1,-1,1],[0,2,0,-1,1,1,-1],[0,2,0,1,-1,-1,1],[0,2,0,1,-1,1,-1],[0,2,0,1,1,-1,-1],[0,2,1,-1,-1,0,1],[0,2,1,-1,-1,1,0],[0,2,1,-1,0,-1,1],[0,2,1,-1,0,1,-1],[0,2,1,-1,1,-1,0],[0,2,1,-1,1,0,-1],[0,2,1,0,-1,-1,1],[0,2,1,0,-1,1,-1],[0,2,1,0,1,-1,-1],[0,2,1,1,-1,-1,0],[0,2,1,1,-1,0,-1],[0,2,1,1,0,-1,-1],[1,-1,-1,0,0,1,2],[1,-1,-1,0,0,2,1],[1,-1,-1,0,1,0,2],[1,-1,-1,0,1,2,0],[1,-1,-1,0,2,0,1],[1,-1,-1,0,2,1,0],[1,-1,-1,1,0,0,2],[1,-1,-1,1,0,2,0],[1,-1,-1,1,2,0,0],[1,-1,-1,2,0,0,1],[1,-1,-1,2,0,1,0],[1,-1,-1,2,1,0,0],[1,-1,0,-1,0,1,2],[1,-1,0,-1,0,2,1],[1,-1,0,-1,1,0,2],[1,-1,0,-1,1,2,0],[1,-1,0,-1,2,0,1],[1,-1,0,-1,2,1,0],[1,-1,0,0,-1,1,2],[1,-1,0,0,-1,2,1],[1,-1,0,0,1,-1,2],[1,-1,0,0,1,2,-1],[1,-1,0,0,2,-1,1],[1,-1,0,0,2,1,-1],[1,-1,0,1,-1,0,2],[1,-1,0,1,-1,2,0],[1,-1,0,1,0,-1,2],[1,-1,0,1,0,2,-1],[1,-1,0,1,2,-1,0],[1,-1,0,1,2,0,-1],[1,-1,0,2,-1,0,1],[1,-1,0,2,-1,1,0],[1,-1,0,2,0,-1,1],[1,-1,0,2,0,1,-1],[1,-1,0,2,1,-1,0],[1,-1,0,2,1,0,-1],[1,-1,1,-1,0,0,2],[1,-1,1,-1,0,2,0],[1,-1,1,-1,2,0,0],[1,-1,1,0,-1,0,2],[1,-1,1,0,-1,2,0],[1,-1,1,0,0,-1,2],[1,-1,1,0,0,2,-1],[1,-1,1,0,2,-1,0],[1,-1,1,0,2,0,-1],[1,-1,1,2,-1,0,0],[1,-1,1,2,0,-1,0],[1,-1,1,2,0,0,-1],[1,-1,2,-1,0,0,1],[1,-1,2,-1,0,1,0],[1,-1,2,-1,1,0,0],[1,-1,2,0,-1,0,1],[1,-1,2,0,-1,1,0],[1,-1,2,0,0,-1,1],[1,-1,2,0,0,1,-1],[1,-1,2,0,1,-1,0],[1,-1,2,0,1,0,-1],[1,-1,2,1,-1,0,0],[1,-1,2,1,0,-1,0],[1,-1,2,1,0,0,-1],[1,0,-1,-1,0,1,2],[1,0,-1,-1,0,2,1],[1,0,-1,-1,1,0,2],[1,0,-1,-1,1,2,0],[1,0,-1,-1,2,0,1],[1,0,-1,-1,2,1,0],[1,0,-1,0,-1,1,2],[1,0,-1,0,-1,2,1],[1,0,-1,0,1,-1,2],[1,0,-1,0,1,2,-1],[1,0,-1,0,2,-1,1],[1,0,-1,0,2,1,-1],[1,0,-1,1,-1,0,2],[1,0,-1,1,-1,2,0],[1,0,-1,1,0,-1,2],[1,0,-1,1,0,2,-1],[1,0,-1,1,2,-1,0],[1,0,-1,1,2,0,-1],[1,0,-1,2,-1,0,1],[1,0,-1,2,-1,1,0],[1,0,-1,2,0,-1,1],[1,0,-1,2,0,1,-1],[1,0,-1,2,1,-1,0],[1,0,-1,2,1,0,-1],[1,0,0,-1,-1,1,2],[1,0,0,-1,-1,2,1],[1,0,0,-1,1,-1,2],[1,0,0,-1,1,2,-1],[1,0,0,-1,2,-1,1],[1,0,0,-1,2,1,-1],[1,0,0,1,-1,-1,2],[1,0,0,1,-1,2,-1],[1,0,0,1,2,-1,-1],[1,0,0,2,-1,-1,1],[1,0,0,2,-1,1,-1],[1,0,0,2,1,-1,-1],[1,0,1,-1,-1,0,2],[1,0,1,-1,-1,2,0],[1,0,1,-1,0,-1,2],[1,0,1,-1,0,2,-1],[1,0,1,-1,2,-1,0],[1,0,1,-1,2,0,-1],[1,0,1,0,-1,-1,2],[1,0,1,0,-1,2,-1],[1,0,1,0,2,-1,-1],[1,0,1,2,-1,-1,0],[1,0,1,2,-1,0,-1],[1,0,1,2,0,-1,-1],[1,0,2,-1,-1,0,1],[1,0,2,-1,-1,1,0],[1,0,2,-1,0,-1,1],[1,0,2,-1,0,1,-1],[1,0,2,-1,1,-1,0],[1,0,2,-1,1,0,-1],[1,0,2,0,-1,-1,1],[1,0,2,0,-1,1,-1],[1,0,2,0,1,-1,-1],[1,0,2,1,-1,-1,0],[1,0,2,1,-1,0,-1],[1,0,2,1,0,-1,-1],[1,1,-1,-1,0,0,2],[1,1,-1,-1,0,2,0],[1,1,-1,-1,2,0,0],[1,1,-1,0,-1,0,2],[1,1,-1,0,-1,2,0],[1,1,-1,0,0,-1,2],[1,1,-1,0,0,2,-1],[1,1,-1,0,2,-1,0],[1,1,-1,0,2,0,-1],[1,1,-1,2,-1,0,0],[1,1,-1,2,0,-1,0],[1,1,-1,2,0,0,-1],[1,1,0,-1,-1,0,2],[1,1,0,-1,-1,2,0],[1,1,0,-1,0,-1,2],[1,1,0,-1,0,2,-1],[1,1,0,-1,2,-1,0],[1,1,0,-1,2,0,-1],[1,1,0,0,-1,-1,2],[1,1,0,0,-1,2,-1],[1,1,0,0,2,-1,-1],[1,1,0,2,-1,-1,0],[1,1,0,2,-1,0,-1],[1,1,0,2,0,-1,-1],[1,1,2,-1,-1,0,0],[1,1,2,-1,0,-1,0],[1,1,2,-1,0,0,-1],[1,1,2,0,-1,-1,0],[1,1,2,0,-1,0,-1],[1,1,2,0,0,-1,-1],[1,2,-1,-1,0,0,1],[1,2,-1,-1,0,1,0],[1,2,-1,-1,1,0,0],[1,2,-1,0,-1,0,1],[1,2,-1,0,-1,1,0],[1,2,-1,0,0,-1,1],[1,2,-1,0,0,1,-1],[1,2,-1,0,1,-1,0],[1,2,-1,0,1,0,-1],[1,2,-1,1,-1,0,0],[1,2,-1,1,0,-1,0],[1,2,-1,1,0,0,-1],[1,2,0,-1,-1,0,1],[1,2,0,-1,-1,1,0],[1,2,0,-1,0,-1,1],[1,2,0,-1,0,1,-1],[1,2,0,-1,1,-1,0],[1,2,0,-1,1,0,-1],[1,2,0,0,-1,-1,1],[1,2,0,0,-1,1,-1],[1,2,0,0,1,-1,-1],[1,2,0,1,-1,-1,0],[1,2,0,1,-1,0,-1],[1,2,0,1,0,-1,-1],[1,2,1,-1,-1,0,0],[1,2,1,-1,0,-1,0],[1,2,1,-1,0,0,-1],[1,2,1,0,-1,-1,0],[1,2,1,0,-1,0,-1],[1,2,1,0,0,-1,-1],[2,-1,-1,0,0,1,1],[2,-1,-1,0,1,0,1],[2,-1,-1,0,1,1,0],[2,-1,-1,1,0,0,1],[2,-1,-1,1,0,1,0],[2,-1,-1,1,1,0,0],[2,-1,0,-1,0,1,1],[2,-1,0,-1,1,0,1],[2,-1,0,-1,1,1,0],[2,-1,0,0,-1,1,1],[2,-1,0,0,1,-1,1],[2,-1,0,0,1,1,-1],[2,-1,0,1,-1,0,1],[2,-1,0,1,-1,1,0],[2,-1,0,1,0,-1,1],[2,-1,0,1,0,1,-1],[2,-1,0,1,1,-1,0],[2,-1,0,1,1,0,-1],[2,-1,1,-1,0,0,1],[2,-1,1,-1,0,1,0],[2,-1,1,-1,1,0,0],[2,-1,1,0,-1,0,1],[2,-1,1,0,-1,1,0],[2,-1,1,0,0,-1,1],[2,-1,1,0,0,1,-1],[2,-1,1,0,1,-1,0],[2,-1,1,0,1,0,-1],[2,-1,1,1,-1,0,0],[2,-1,1,1,0,-1,0],[2,-1,1,1,0,0,-1],[2,0,-1,-1,0,1,1],[2,0,-1,-1,1,0,1],[2,0,-1,-1,1,1,0],[2,0,-1,0,-1,1,1],[2,0,-1,0,1,-1,1],[2,0,-1,0,1,1,-1],[2,0,-1,1,-1,0,1],[2,0,-1,1,-1,1,0],[2,0,-1,1,0,-1,1],[2,0,-1,1,0,1,-1],[2,0,-1,1,1,-1,0],[2,0,-1,1,1,0,-1],[2,0,0,-1,-1,1,1],[2,0,0,-1,1,-1,1],[2,0,0,-1,1,1,-1],[2,0,0,1,-1,-1,1],[2,0,0,1,-1,1,-1],[2,0,0,1,1,-1,-1],[2,0,1,-1,-1,0,1],[2,0,1,-1,-1,1,0],[2,0,1,-1,0,-1,1],[2,0,1,-1,0,1,-1],[2,0,1,-1,1,-1,0],[2,0,1,-1,1,0,-1],[2,0,1,0,-1,-1,1],[2,0,1,0,-1,1,-1],[2,0,1,0,1,-1,-1],[2,0,1,1,-1,-1,0],[2,0,1,1,-1,0,-1],[2,0,1,1,0,-1,-1],[2,1,-1,-1,0,0,1],[2,1,-1,-1,0,1,0],[2,1,-1,-1,1,0,0],[2,1,-1,0,-1,0,1],[2,1,-1,0,-1,1,0],[2,1,-1,0,0,-1,1],[2,1,-1,0,0,1,-1],[2,1,-1,0,1,-1,0],[2,1,-1,0,1,0,-1],[2,1,-1,1,-1,0,0],[2,1,-1,1,0,-1,0],[2,1,-1,1,0,0,-1],[2,1,0,-1,-1,0,1],[2,1,0,-1,-1,1,0],[2,1,0,-1,0,-1,1],[2,1,0,-1,0,1,-1],[2,1,0,-1,1,-1,0],[2,1,0,-1,1,0,-1],[2,1,0,0,-1,-1,1],[2,1,0,0,-1,1,-1],[2,1,0,0,1,-1,-1],[2,1,0,1,-1,-1,0],[2,1,0,1,-1,0,-1],[2,1,0,1,0,-1,-1],[2,1,1,-1,-1,0,0],[2,1,1,-1,0,-1,0],[2,1,1,-1,0,0,-1],[2,1,1,0,-1,-1,0],[2,1,1,0,-1,0,-1],[2,1,1,0,0,-1,-1]]
print(aws)
