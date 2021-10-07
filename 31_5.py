class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        p = len(nums) - 1
        while p >= 1 and nums[p] <= nums[p - 1]:
            p -= 1

        if p > 0:
            for i in list(reversed(range(p, len(nums)))):
                if nums[i] > nums[p - 1]:
                    nums[i], nums[p - 1] = nums[p - 1], nums[i]
                    break

        l = p
        n = len(nums) - 1
        while l < n:
            nums[l], nums[n] = nums[n], nums[l]
            l += 1
            n -= 1

        return nums
