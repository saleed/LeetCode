class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        s=set()
        for i in range(len(nums[:k])):
            if nums in s:
                return False
            s.add(nums[i])

        p=k
        while p<len(nums):
            s.remove(nums[p-k])
            if nums[p] in s:
                return False
        return True