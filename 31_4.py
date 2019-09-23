

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for j in range(1,len(nums))[::-1]:
            if nums[j]<nums[j-1]:
                continue
            else:
                for i in range(j,len(nums))[::-1]:
                    if nums[i]>nums[j-1]:
                        nums[i],nums[j-1]=nums[j-1],nums[i]
                        break
                break
