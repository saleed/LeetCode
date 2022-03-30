class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res=self.nonRecursive(nums)
        return res

    def recursive(self,nums,i,res):
        if i>=len(nums):
            res.append(nums[:])
            return
        self.recursive(nums,i+1,res)
        for v in range(i+1,len(nums)):
            if nums[v]==nums[i]:
                continue
            nums[v],nums[i]=nums[i],nums[v]
            self.recursive(nums,i+1,res)
            nums[i],nums[v]=nums[v],nums[i]


    def nonRecursive(self,nums):
        res=[]
        nums.sort()
        while True:
            res.append(nums[:])
            p=len(nums)-1
            while p>0 and nums[p]<nums[p-1]:
                p-=1

            if p==0:
                break
            q=len(nums)-1
            swap=p-1
            while q>swap and nums[q]<nums[swap]:
                q-=1
            nums[q],nums[swap]=nums[swap],nums[q]

            q=len(nums)-1
            while p<q:
                nums[p],nums[q]=nums[q],nums[p]
                p+=1
                q-=1
        return res




a=Solution()
print(a.permute([2,3,1,4]))

