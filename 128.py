class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        # vis=set()
        best=0
        for i in s:
            if i-1 not in nums:
                y=i+1   
                while y in s:
                    # vis.add(y)
                    y+=1
                best=max(best,y-i)
        return best




