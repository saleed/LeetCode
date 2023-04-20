class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.slove2(nums,target)


    def slove1(self,nums,target):
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                return [i,nums[i+1:].index(target-nums[i])+i+1]

    def slove2(self,nums,target):
        ndict=dict(zip(nums,[i for i in range(len(nums))]))
        for i in range(len(nums)):
            if target-nums[i] in ndict and ndict[target-nums[i]]!=i:
                return [i,ndict[target-nums[i]]]
