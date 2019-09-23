class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        res=[]
        nums.append(float("inf"))
        start=0
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                continue
            else:
                if i-start>=1:
                    res.append(str(nums[start])+"->"+str(nums[i]))
                else:
                    res.append(str(nums[start]))
                start=i+1

        return res


test= [0,1,2,4,5,7]
a=Solution()
print(a.summaryRanges(test))




