class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        self.recursive(nums, 0, res)
        return res

    def recursive(self, nums, i, res):
        print(nums,i)
        if i >= len(nums):
            res.append(nums[:])
            return

        select=set()
        for j in range(i, len(nums)):
            if nums[j] not in  select:
                nums[i], nums[j] = nums[j], nums[i]
                self.recursive(nums, i + 1, res)
                nums[j], nums[i] = nums[i], nums[j]
                select.add(nums[j])





nums = [1,1,2]
a=Solution()
print a.permuteUnique(nums)