class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        half = len(nums[::2])
        # nums[::2], nums[1::2] = nums[:half], nums[half:]
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

        #how to new the mean of [::-1]
        #for example [a,b]+[c,d] a sorted array,by using [::-1] we can get the result is b,d,c,a we can assure that between b,d, d,c c,a they must not neghborhood
        #on contrast without [::-1], we get a,c,b,d    we can not assure the c,b are not neghborhood

    def wiggleSort2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        while i+1<len(nums):
            p=i+1
            while nums[i]!=nums[p] and p<len(nums):
                p+=1
                break
            if p>=len(nums):
                break
            if nums[i]<nums[p]:
                nums[i+1],nums[p]=nums[p],nums[i+1]
            else:
                nums[i],nums[p]=nums[p],nums[i]
            i+=1
            if i+1>=len(nums):
                break
            while nums[i]!=nums[p] and p<len(nums):
                p+=1
                break
            if nums[i]>nums[p]:
                nums[i+1],nums[p]=nums[p],nums[i+1]
            else:
                nums[i],nums[p]=nums[p],nums[i]
            i+=1
        return nums






nums = [1, 5, 1, 1, 6, 4]
a=Solution()
# print a.wiggleSort2(nums)
print nums[::2] #[1, 1, 6]
print nums[::-1]#[4, 6, 1, 1, 5, 1]