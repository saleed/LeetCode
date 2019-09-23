class Solution(object):
    def findDuplicate11(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s=set()
        # for i in nums:
        #     if len(s)==0:
        #         s.add(i)
        #     elif i not in s:
        #         s.remove(i)
        # return list(s)[0]

    def findDuplicate(self, nums):
        #不适用内存，直接使用自己构成哈希表
        for i in range(len(nums)):
            while (nums[i] != i):
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    tmp = nums[i]
                    nums[i] = nums[tmp]
                    nums[tmp] = tmp