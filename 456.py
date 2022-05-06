class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return
        pre=0
        for i in range(1,len(nums)):
            tmp=nums[i]-nums[i-1]
            if tmp==0:
                continue
            else:
                if tmp<0 and pre>0:
                    return True
                else:
                    pre=tmp
        return False


