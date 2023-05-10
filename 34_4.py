class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        p = 0
        q = len(nums) - 1
        while p <= q:
            mid = (p + q) / 2
            if nums[mid] == target:
                q = mid - 1
            elif nums[mid] < target:
                p = mid + 1
            else:
                q = mid - 1
        left = -1
        if q + 1 < len(nums) and nums[q + 1] == target:
            left = q + 1

        p = 0
        q = len(nums) - 1
        while p <= q:
            mid = (p + q) / 2
            if nums[mid] == target:
                p = mid + 1
            elif nums[mid] < target:
                p = mid + 1
            else:
                q = mid - 1
        right = -1
        if p - 1 >= 0 and nums[p - 1] == target:
            right = p - 1

        return [left, right]



