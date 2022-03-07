class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        p=0
        step=1
        while p<len(nums):
            ran=nums[p]
            max_right=-float("inf")
            for i in range(ran+1):
                if p+i<len(nums) and  max_right<p+i+nums[p+i]:
                        max_right=p+i+nums[p+i]

            p=max_right
            step+=1



