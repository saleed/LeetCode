class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        id=len(nums)-k

        while True:
            p=self.findPivot(nums)
            # print(id,p,nums)
            if p==id:
                return nums[p]
            elif p<id:
                id=id-p-1
                nums=nums[p+1:]
            else:
                nums=nums[:p]




    ###快速排
    def findPivot(self,nums):
        pivot=nums[0]
        p=0
        for i in range(1,len(nums)):
            if nums[i]<pivot:
                p+=1
                nums[i],nums[p]=nums[p],nums[i]
            print(p,nums)
        nums[p],nums[0]=nums[0],nums[p]
        # print(">>",nums)
        return p


s=Solution()
test=[3,2,1,5,6,4]
k=2
s.findKthLargest(test,k)