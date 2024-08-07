class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=sum(nums)
        tmps=0
        for i in range(len(nums)):
            if tmps==s-nums[i]-tmps:
                return i
            tmps+=nums[i]
        return -1
