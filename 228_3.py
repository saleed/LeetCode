class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0:
            return []
        res=[]


        nums.append(float("inf"))
        p=0
        for i in range(len(nums)-1):
            if nums[i+1]-1==nums[i]:
                continue
            else:
                if p<i:
                    res.append(str(nums[p])+"->"+str(nums[i]))
                else:
                    res.append(str(nums[i]))
                p=i+1
        return res



test= [0,1,2,4,5,7]
a=Solution()
print(a.summaryRanges(test))

