class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #153题使用了二分的方法，是因为在没有重复元素的条件下，可以很容易判断最小值在左区间和右区间
        #但是在有重复元素的条件下，153方法会有问题
        # 如果允许使用额外内存，可以把nums变成一个没有重复数字的数字再处理
        # 当然也可以使用分治算法

