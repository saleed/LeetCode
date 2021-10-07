# coding:utf-8
# coding:utf-8
# 出发点：从题干上感觉是用遍历，想过通过遍历获取最大值，最小值，但是似乎并不能通过这些特征找到缺失的正数
# 分几种情况，1.nums连续，（1）分布在0的左侧或右侧  （2）分布在0两侧 2.不连续，（1）存在连续部分分布在0两侧 （2）不存在部分分布在0两侧
# 所以关键是看连续部分，是否分布在0的两侧
# 所以关键是要找出最靠近0的连续部分
# 但是显然不能排序，复杂度不允许



#另外一种思路，N个数，缺失的正整数一定是在0到N之间，




class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums):
            j = i
            while nums[j] > 0 and nums[j] <= len(nums) and nums[nums[j] - 1] != nums[j]:
                tmp = nums[nums[j] - 1]
                nums[nums[j] - 1] = nums[j]
                nums[j] = tmp
            i += 1
        print(nums)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


if __name__=="__main__":
    a=Solution()
    nums= [3, 4, -1, 1]
    print(a.firstMissingPositive(nums))



