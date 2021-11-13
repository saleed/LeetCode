class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return 0
        res=nums[0]
        for v in nums[1:]:
            res=res^v
        return res