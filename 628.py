class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)<3:
            return 0
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])