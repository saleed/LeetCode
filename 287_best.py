class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(1,len(nums)):
            if nums[i]==i:
                continue
            p=nums[i]
            while nums[p]!=p:
                tmp=nums[nums[p]]
                nums[nums[p]]=p
                p=tmp




