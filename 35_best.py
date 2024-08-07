class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search1(nums,target)

    #二分查找t
    def search1(self,nums,target):
        p=0
        q=len(nums)-1
        while p<q:
            mid=(p+q)/2
            print(mid)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                p=mid+1
            else:
                q=mid
        if nums[p]<target:
            return p+1
        elif nums[p]>=target:
            return p




