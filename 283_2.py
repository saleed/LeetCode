class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[p]=nums[i]
                p+=1
        while p<len(nums):
            nums[p]=0
            p+=1


