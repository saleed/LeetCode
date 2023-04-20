class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        prei = float("inf")
        prej = float("inf")
        res = []
        for i in range(len(nums) - 1):
            if prei == nums[i]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if prej == nums[j]:
                    continue
                tmp_res = self.twosum(j + 1, len(nums) - 1, nums, target - nums[i] - nums[j])

                for c in tmp_res:
                    res.append([nums[i], nums[j]] + c)
                prej = nums[j]
            prei = nums[i]

        return res

    def twosum(self, i, j, nums, target):
        res = []
        while i < j:
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
                pre = nums[i]
                while i < j and nums[i] == pre:
                    i += 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return res
