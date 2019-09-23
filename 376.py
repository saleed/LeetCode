class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        if len(nums)==0:
            return 0
        high=[1]*len(nums)
        low=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<=nums[i]:
                    high[i]=max(high[i],low[j]+1)
                if nums[j]>=nums[i]:
                    low[i]=max(low[i],high[j]+1)
        maxv=-float("inf")
        for i in range(len(nums)):
            maxv=max(low[i],high[i])

        #better solution as below:
        for i in range(len(nums)):
            if (nums[i] > nums[i - 1]):
                high[i] = low[i - 1] + 1
                low[i] = low[i - 1]
            elif (nums[i] < nums[i - 1]):
                low[i] = high[i - 1] + 1
                high[i] = high[i - 1]
            else:
                low[i] = low[i - 1]
                high[i] = high[i - 1]
        return maxv

        
    


nums=[1,7,4,9,2,5]
a=Solution()
print a.wiggleMaxLength(nums)

