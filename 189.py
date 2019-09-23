class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:]=nums[k+1:]+nums[:k+1] #careful for this
        print nums





a=Solution()
tst=[1,2,3,4,5,6,7]
print a.rotate(tst,3)
