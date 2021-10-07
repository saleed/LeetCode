# coding=utf-8
"""
这个题目的难度在如何证明每次找到一个能到最远位置的下一跳，一定是当前状态下的最优解，也是全局状态下最优解
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0
        minpace = 0
        while p < len(nums) - 1:
            rg = nums[p]
            maxid = 0
            nextid = p + 1
            if rg == 0:
                return 0
            for i in range(p + 1, p + rg + 1):
                if i >= len(nums) - 1:
                    nextid = len(nums)
                    continue
                if i + nums[i] > maxid:
                    maxid = i + nums[i]
                    nextid = i

            p = nextid
            minpace += 1
        return minpace

if __name__=="__main__":
    a=Solution()
    test=[2,3,1,1,4]
    print(a.jump(test))





