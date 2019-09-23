class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict={}
        for i in nums:
            if i in dict.keys():
                del dict[i]
            else:
                dict[i]=1
        return dict.keys()