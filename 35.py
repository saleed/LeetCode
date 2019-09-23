class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1

        # while left<right:
        #     mid=(left+right)/2
        #     if nums[mid]==target:
        #         return mid
        #     elif nums[mid]<target:
        #         left=mid+1
        #     else:
        #         right=mid
        # return left

        while left <= right:  ##如果这里的条件是小于等于
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid-1 ###while中的条件为小于等于，则这里的条件必须是mid-1,否则可能死循环
        return left

