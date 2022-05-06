class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        s=set()
        for v in nums:
            if v not in s:
                s.add(v)
            else:
                s.remove(v)
        return list(s)