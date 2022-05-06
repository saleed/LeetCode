class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        avg=float(sum(nums)/len(nums))
        if avg-int(avg)>0.5:
            avg=avg+1
        res=0
        for i in nums:
            res+=int(abs(i-avg))
        return res
