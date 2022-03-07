class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        p=len(nums)-1
        while p>0 and nums[p]<=nums[p-1]:
            p-=1
        pos=p-1
        print(pos)
        if pos>=0:
            q=len(nums)-1
            while q>pos and nums[pos]>=nums[q]:
                q-=1
            nums[q],nums[pos]=nums[pos],nums[q]
        p=pos+1
        q=len(nums)-1

        while p<q:
            nums[q],nums[p]=nums[p],nums[q]
            p+=1
            q-=1
a=Solution()
print(a.nextPermutation([1,2]))