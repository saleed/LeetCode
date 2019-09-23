class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return nums
        curnum=0
        pre=-1
        p=0
        q=0
        while q<len(nums):
            if nums[q]!=pre:
                curnum=1
                nums[p]=nums[q]
                p+=1
                pre=nums[q]
            elif curnum==1:
                curnum+=1
                nums[p]=nums[q]
                p+=1
            q+=1
        return p

a=Solution()
nums = [1,1,1,2,2,3]

print(a.removeDuplicates(nums))
