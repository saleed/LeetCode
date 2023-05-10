
#####

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        p = 0
        q = len(nums) - 1


        # while p < q:
        #     mid = (p + q) / 2
        #     if nums[mid] == target:
        #         if nums[mid + 1] == target:##先寻找右边界，如果遇到mid为target时候，需要判断左边界是否可以往右移，因为p有可能等于mid，
        #             p = mid + 1
        #         else:
        #             q = mid
        #     elif nums[mid] < target:
        #         p = mid + 1
        #     else:
        #         q = mid


        ##替换掉上面更便捷的方法：
        ##目的是假如nums[mid] == target 是否能直接使用mid更新左边界，左边界不能和mid相等
        while p < q:
            mid = (p + q) / 2+1  ###tricks 把mid往q上靠
            if nums[mid] == target:
                p=mid
            elif nums[mid] < target:
                p = mid
            else:
                q = mid-1


        if nums[p] != target:
            right = -1
        else:
            right = p

        p = 0
        q = len(nums) - 1
        while p < q:
            mid = (p + q) / 2
            if nums[mid] == target:
                q = mid
            elif nums[mid] < target:
                p = mid + 1
            else:
                q = mid

        if nums[p] != target:
            left = -1
        else:
            left = p
        return [left, right]





