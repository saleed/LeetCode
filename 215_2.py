class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        part=self.partition(nums)
        if part==len(nums)-k:
            return nums[part]
        elif part>len(nums)-k:
            self.findKthLargest(nums[:part],k)
        else:
            self.findKthLargest(nums[part+1:],k-part-1)




    def partition(self,nums):
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return 0
        p=0
        for i in range(len(nums)):
           if nums[i]<nums[-1]:
               nums[p],nums[i]=nums[i],nums[p]
               p+=1

        nums[p],nums[-1]=nums[-1],nums[p]
        return p