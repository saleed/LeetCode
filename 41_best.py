class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #
        p=0
        while p<len(nums):
            pval=nums[p]
            while pval>=1 and pval <=len(nums) and nums[pval-1]!=pval:
                tmp=nums[pval-1]
                nums[pval-1]=pval
                pval=tmp
            p+=1

        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1





