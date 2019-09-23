class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        if len(nums)==0:
            return False
        for i in range(len(nums)):
            if nums[i] in d:
                if abs(i-d[nums[i]])<=k:
                    return True
            d[nums[i]]=i
        return False