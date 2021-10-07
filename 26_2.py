class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        p=0
        for i in range(len(nums)):
            if nums[i]!=nums[p]:
                p+=1
                nums[p]=nums[i]
        return p+1