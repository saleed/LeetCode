class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        id=0
        i=0
        while i<len(nums):
            if nums[i]!=val:
                nums[id]=nums[i]
                id+=1
            i+=1
        return id