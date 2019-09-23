class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        # res=self.recursive(nums)

        res=[]
        self.recursive2(nums,0,res)

        return res



    #建立规模为n 和规模为n-1子问题之间的关系，
    def recursive(self,nums):
        if len(nums)==1:
            return [[nums[0]]]
        res=[]
        for i in range(len(nums)):
            nums[0],nums[i]=nums[i],nums[0]
            nextres=self.recursive(nums[1:])
            for j in nextres:
                tmp=[nums[0]]
                tmp.extend(j)
                res.append(tmp)
        return res


    #模拟的思想，从第一位开始考虑怎么选择
    def recursive2(self,nums,id,res):
        if id==len(nums):
            res.append(nums[:])
        for j in range(id,len(nums)):
            nums[j],nums[id]=nums[id],nums[j]  #这个交换操作的目的是要把需要的数字移到首位，不需要的数字无论扔除了首位的在哪个位置都可以
            self.recursive2(nums,id+1,res)
            nums[id],nums[j]=nums[j],nums[id]

nums=[1,2,3]
a=Solution()
print(a.permute(nums))




