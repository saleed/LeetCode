#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/11 13:37
# @Author  : sunaolin
# @File    : 698.py


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k != 0:
            return False

        nums.sort()

        nums = nums[::-1]
        print(sum(nums))
        if nums[0] > sum(nums) / k:
            return False
        dp = {}

        ret = self.dfs(nums, 0, k, 0, sum(nums) / k, dp)
        print(dp)
        return ret

    ##增加存储的部分，记忆化搜索，直接复用nums做状态表示

    ##举个例子说明为啥会重复，nums=[1,2,3,4]
    # 先选1再选2和先选2再选1是重复的
    def dfs(self, nums, i, k, tmplen, target, dp):

        if i == k:
            return True
        if tuple(nums) in dp:
            return dp[tuple(nums)]
        if tmplen > target:
            ret = False
        elif tmplen == target:
            return self.dfs(nums, i + 1, k, 0, target, dp)
        else:
            ret = False
            for j in range(len(nums)):
                if nums[j] == 0:
                    continue
                tmp = nums[j]
                nums[j] = 0
                ret = self.dfs(nums, i, k, tmplen + tmp, target, dp)
                nums[j] = tmp
                if ret:
                    break
        dp[tuple(nums)] = ret
        return ret

