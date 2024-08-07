class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #############
        l=0
        left=float("inf")
        i=1
        while i<len(nums):
            if nums[i]<nums[i-1]:
                start=i-1
                while i+1<len(nums) and nums[i+1]==nums[i]:
                    i+=1
                left=min(left,start)

                while left>=0 and nums[left]>nums[i]:
                    left-=1
                l=max(l,i-left)
            i+=1
        return l

test=[1,3,2,2,2]
ss=Solution()
print(ss.findUnsortedSubarray(test))