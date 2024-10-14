class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        p=0
        q=0
        r=len(nums)-1

        while q<r:
            if nums[q]==0:
                nums[q],nums[p]=nums[p],nums[q]  ###换过来的一定是个1
                p+=1
                q+=1
            elif nums[q]==1: ##遇到1直接跳过
                q+=1
            else:
                nums[q], nums[r] = nums[r], nums[q]
                r -= 1
        print(nums)



nums = [2,0,2,1,1,0]

a=Solution()
print(a.sortColors(nums))