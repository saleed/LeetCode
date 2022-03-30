class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        prefixsum={}

        maxl=0
        for i in range(len(nums)):
            sumval=prefixsum[i-1]+nums[i] if i>0 else nums[i]
            if sumval not in prefixsum:
                prefixsum[sumval]=i
            if sumval==k:
                maxl=max(maxl,i+1)
            if sumval-k in prefixsum:
                maxl=max(maxl,i-prefixsum[sumval-k])
        return maxl
