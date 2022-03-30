class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        for i in range(len(nums)):
            while nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i-1]]
            if nums[i]!=i+1:
                return nums[i]


a=Solution()

t=[1,3,4,2,2]
print(a.findDuplicate(t))