class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        value=[0]*len(nums)
        value[0]=nums[0]
        value[1]=nums[1]
        for i in range(2,len(nums)):
            for j in range(i-1):
                value[i]=max(value[j]+nums[i],value[i])  #value(k) means the max rob value ended with house k
        return max(value)

    # f(0) = nums[0]
    # f(1) = max(num[0], num[1])
    # f(k) = max(f(k - 2) + nums[k], f(k - 1)) f(k) means the max rob value from 0 to k
    def rob2(self,nums):

        last, now = 0, 0

        for i in nums: last, now = now, max(last + i, now)

        return now