class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()

        for i in range(len(nums)):
            if i%3==1:
                nums[i],nums[i-1]=nums[i-1],nums[i]
        return nums

