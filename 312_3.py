#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/12 14:11
# @Author  : sunaolin
# @File    : 312_3.py

"""
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。

 

示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
示例 2：

输入：nums = [1,5]
输出：10

假设这个区间是个开区间，最左边索引 i，最右边索引 j
我这里说 “开区间” 的意思是，我们只能戳爆 i 和 j 之间的气球，i 和 j 不要戳
DP思路是这样的，就先别管前面是怎么戳的，你只要管这个区间最后一个被戳破的是哪个气球
这最后一个被戳爆的气球就是 k
注意！！！！！
k是这个区间   最后一个   被戳爆的气球！！！！！
k是这个区间   最后一个   被戳爆的气球！！！！！
假设最后一个被戳爆的气球是粉色的，k 就是粉色气球的索引
然后由于 k 是最后一个被戳爆的，所以它被戳爆之前的场景是什么亚子？
是这样子的朋友们！因为是最后一个被戳爆的，所以它周边没有球了！没有球了！只有这个开区间首尾的 i 和 j 了！！
这就是为什么DP的状态转移方程是只和 i 和 j 位置的数字有关
假设 dp[i][j] 表示开区间 (i,j) 内你能拿到的最多金币
那么这个情况下
你在 (i,j) 开区间得到的金币可以由 dp[i][k] 和 dp[k][j] 进行转移
如果你此刻选择戳爆气球 k，那么你得到的金币数量就是：
total= dp[i][k]+val[i] * val[k] * val[j]+dp[k][j]
注：val[i] 表示 i 位置气球的数字
然后 (i,k) 和 (k,j) 也都是开区间

"""

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[1]+nums+[1]
        dp=[[0 for _ in range(len(nums))] for _ in range(len(nums))]

    ###牛逼一次过，核心是首位加上1  dp[i][j]是开区间才行！！！！！
        for itv in range(len(nums)):
            for i in range(len(nums)):
                if i+itv>=len(nums):
                    continue
                if itv==0 or itv==1:
                    dp[i][i+itv]=0
                else:
                    for k in range(i+1,i+itv):
                        dp[i][i+itv]=max(dp[i][i+itv],dp[i][k]+dp[k][i+itv]+nums[i]*nums[k]*nums[i+itv])
        return dp[0][-1]

