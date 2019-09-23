class Solution(object):

    #naive O(n**2) algorithm
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        count=0
        sumto=[0]*len(nums)
        sumto[0]=nums[0]
        for i in range(1,len(nums)):
            sumto[i]=sumto[i-1]+nums[i]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                betsum=sumto[j]-sumto[i]+nums[i]
                if betsum<=upper and betsum>=lower:
                    count+=1
        return count

    def countRangeSum2(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        mergesort()!!!
