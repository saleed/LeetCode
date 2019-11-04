import heapq

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return min(nums)

        return heapq.nlargest(3,nums)[-1]






a=Solution()
nums=[1,2,3,4]
print(a.thirdMax(nums))
print(nums)