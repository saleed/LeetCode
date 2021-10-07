class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p=0
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            else:
                nums[p]=nums[i]
                p+=1
        return p