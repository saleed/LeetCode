class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return i
        return 0
