class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p=0
        q=len(nums)-1
        while p<=q:
            mid=(p+q)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                p=mid+1
            else:
                q=mid-1
        return min(p,q)