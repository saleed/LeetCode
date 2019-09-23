class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #哈希表的思路，但是哈希表又不能新开辟内存，所以直接使用nums的内存，
        for i in range(len(nums)):
            j=i
            # print(j)
            # while nums[j]>0 and nums[j]<=len(nums) and nums[j]!= j+1:
            while nums[j] > 0 and nums[j] <= len(nums) and nums[nums[j]-1] != nums[j]:
                # print(j,nums[j])
                # nums[j],nums[nums[j]-1]=nums[nums[j]-1],nums[j]
                tmp=nums[nums[j]-1]
                nums[nums[j]-1]=nums[j]
                nums[j]=tmp
        print(nums)

        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1



a=Solution()
# test1=[1,2,0]
# print(a.firstMissingPositive(test1))
test2=[-1,4,2,1,9,10]
print(a.firstMissingPositive(test2))
