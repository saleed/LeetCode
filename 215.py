import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k==0:
            return 0
        res=heapq.nlargest(k,nums)
        heapq.heapify(nums)
        heapq.nlargest(k,nums)
        heapq.nsmallest(k,nums)
        return res[-1]



test=[2,4,7,8,41,32,23,6]
new=heapq.nlargest(3,test)
print new
