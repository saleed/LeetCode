## coding:UTF-8


#找到target后，继续二分查找
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.binary(nums,target)
