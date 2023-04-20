class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lost = -1
        sumv = 0
        for i in range(1, len(nums) + 1):
            if i not in nums:
                lost = i
            sumv += nums[i - 1]

        return [lost - (len(nums) + 1) * len(nums) / 2 + sumv, lost]






