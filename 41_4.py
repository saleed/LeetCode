class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i<len(nums):
            while 0<nums[i]<=len(nums) and nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]: ##三个条件
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1