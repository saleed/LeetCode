class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        pre = float("inf")
        for i in range(len(nums)):
            if nums[i] == pre:
                continue
            two_sum = self.twosum(i + 1, len(nums) - 1, -nums[i], nums)
            # print(two_sum)
            for r in two_sum:
                res.append([nums[i]] + r)
            pre = nums[i]  ##注意这里去重
        return res

    def twosum(self, i, j, target, nums):
        res = []
        while i < j:
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
                pre = nums[i]
                while i < j and nums[i] == pre:  ##注意这里也要去重
                    i += 1

            while i < j and nums[i] + nums[j] < target:
                i += 1
            while i < j and nums[i] + nums[j] > target:
                j -= 1
        return res