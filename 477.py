class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in range(30):
            c=0
            for v in nums:
                c+=(v>>i)&1
            res+=c*(len(nums)-c)
        return res
    

