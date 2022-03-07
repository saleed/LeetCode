class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        p=0
        q=len(nums)-1
        if target not in nums:
            return [-1,-1]
        while p<q:
            mid=(p+q)/2
            if nums[mid]>=target:
                q=mid  ## cant write q=mid-1 this will cause the q not hit target
            else:
                p=mid+1
        left=p if nums[p]==target else p+1

        p = 0
        q = len(nums) - 1
        while p < q:
            mid = (p + q) / 2
            if nums[mid] <= target:
                p=mid+1  ## cant write q=mid-1 this will cause the q not hit target
            else:
                q=mid
        right=p if nums[p]==target else p-1

        return [left,right]



