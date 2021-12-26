class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k=len(nums)-k+1
        print(k)
        while True:
            left=self.partition(nums)
            print(left, k, nums)
            if left==k:
                return nums[left-1]
            elif left<k:
                nums=nums[left:]
                k=k-(left)
            else:
                nums=nums[:left-1]

    def partition(self,nums):  ##return 到基准值的时候，左边剩下几个数
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1

        pivot=nums[0]
        j=1

        for i in range(1,len(nums)):
            if nums[i]<pivot:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1



        nums[j-1],nums[0]=nums[0],nums[j-1]
        print(j, nums)
        return j



a=Solution()
test=[3,2,1,5,6,4]
k=2

# test=[1]
# k=1

print(a.findKthLargest(test,k))