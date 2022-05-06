class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        down=[1]*len(nums)
        up=[1]*len(nums)

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                up[i]=max(up[i-1],down[i-1]+1)
                down[i]=down[i-1]
            elif nums[i]<nums[i-1]:
                down[i]=max(down[i-1],up[i-1]+1)
                up[i]=up[i-1]
            else:
                down[i]=down[i-1]
                up[i]=up[i-1]
        return max(up[-1],down[-1])