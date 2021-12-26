class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        res=[]
        s=0
        nums.append(float("inf"))
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]!=1:
                if i-1-s>=1:
                    res.append(str(nums[s])+"->"+str(nums[i-1]))
                else:
                    res.append(str(s))
                s=i

        return res

