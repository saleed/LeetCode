class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen=[0]*len(nums)+1

        for i in range(1,len(nums)+1):
            maxlen[i]=max(maxlen[i-1]+nums[i-1],nums[i-1])
        return max(maxlen)



