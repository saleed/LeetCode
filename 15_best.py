class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        p = 0
        while p < len(nums):
            target = -nums[p]
            twosumres = self.twosum(nums, p + 1, len(nums) - 1, target)
            for v in twosumres:
                tmp = [nums[p]]
                tmp.extend(v)
                res.append(tmp)
            while p + 1 < len(nums) and nums[p + 1] == nums[p]:
                p += 1
            p += 1
        return res

    def twosum(self, nums, i, j, target):

        p = i
        q = j
        res = []
        if i >= j:
            return []

        while p < q:
            if nums[p] + nums[q] == target:
                res.append([nums[p], nums[q]])
                while p<q and nums[p] == nums[p + 1] and nums[q - 1] == nums[q]:
                    print(p, q)
                    p += 1
                    q -= 1
                p += 1
                q -= 1
            elif nums[p] + nums[q] < target:

                while  p<q and  nums[p] == nums[p + 1] :
                    p += 1
                p += 1
            else:

                while p < q and  nums[q - 1] == nums[q] :
                    q -= 1
                q -= 1
        return res


a=Solution()
nums = [-1,0,1,2,-1,-4]
print(a.threeSum(nums))