class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict={}
        for i in nums:
            if dict.has_key(i):
                return True
            else:
                dict[i]=0
        return False
