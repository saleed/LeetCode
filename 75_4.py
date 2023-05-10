class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p=0
        q=len(nums)-1
        i=0
        while i<q:######如果这里不限制 当i>q的时候会把尾部已经排好的2全部交换到1的位置
            print(nums)
            if nums[i]==0:
                nums[p],nums[i]=nums[i],nums[p]
                p+=1
                i+=1
            elif nums[i]==2:
                nums[q],nums[i]=nums[i],nums[q]
                q-=1
            else:
                i+=1
        return nums