class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p=0
        while p<len(nums):
            if p+1<len(nums) and nums[p]>nums[p+1]
