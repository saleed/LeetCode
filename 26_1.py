class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=1
        p=1
        while p<len(nums):
            if nums[p]!=nums[p-1]:
                nums[left]=nums[p]
                left+=1
            p+=1
        return nums[:left+1]
