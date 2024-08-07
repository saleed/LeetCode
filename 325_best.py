class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum={}
        maxl=0
        sumv=0
        for i in range(len(nums)):
            sumv+=nums[i]
            if sumv==k:
                maxl=max(maxl,i+1)
            elif sumv-k in presum:
                maxl=max(maxl,i-presum[sumv-k])
            if sumv not in presum:
                presum[sumv]=i
        return maxl