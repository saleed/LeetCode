class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p=-1
        q=len(nums)
        cur=0
        while cur<q:
            if nums[cur]==0:
                p+=1
                nums[cur],nums[p]=nums[p],nums[cur]
                if cur==p:  ###想一想这个是为什么？？
                    cur+=1
            elif nums[cur]==2:
                q-=1
                nums[cur],nums[q]=nums[q],nums[cur]
            else:
                cur+=1




