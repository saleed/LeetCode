class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0:
            return []
        res=[]
        s=0
        nums.append(float("inf")) #####be careful for this
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if i-1>s:
                    res.append(str(nums[s])+"->"+str(nums[i-1]))
                else:
                    res.append(str(nums[s]))
                s=i
        return res
