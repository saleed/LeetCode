class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums)==0:
            return
        sumto=[0]*len(nums)
        sumto[0]=nums[0]
        for i in range(1,len(nums)):
            sumto[i]=sumto[i-1]+nums[i]
        self.sumto=sumto
        self.nums=nums
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if len(self.nums)==0:
            return 0
        return self.sumto[j]-self.sumto[i]+self.nums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)