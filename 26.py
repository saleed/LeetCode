class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return nums

        p=0
        q=0
        while q<len(nums):
            if nums[p]!=nums[q]:
                p+=1
                nums[p]=nums[q]
            q+=1
        return p+1
