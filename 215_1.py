class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k=len(nums)-k
        left, p = self.quicksearch(nums, k)
        while left+1!=k:
            print(left,p,k,nums)
            if left+1>k:
                nums=nums[:left]
            else:
                nums=nums[left:]
                k=k-left-1
            left,p=self.quicksearch(nums,k)

        return p

    def quicksearch(self,nums,k):
        if len(nums)<k:
            return
        pivot=nums[0]
        i=1
        j=1
        while j<len(nums):
            if nums[j]<pivot:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
            j+=1
        nums[i-1],nums[0]=nums[0],nums[i-1]
        return i-1,pivot

s=Solution()
test=[3,2,3,1,2,4,5,5,6]
print(s.findKthLargest(test,4))