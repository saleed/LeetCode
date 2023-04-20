class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        minavg=float("inf")
        tmpsum=0
        for i in range(len(nums)):
            if i<=k:
                tmpsum+=nums[i]
            else:
                minavg=min(minavg,float(tmpsum)/float(k))
                tmpsum+=nums[i]
                tmpsum-=nums[i-k]
        minavg=min(minavg,float(tmpsum)/float(k))
        return minavg
