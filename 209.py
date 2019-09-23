class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """


        #滑动窗口，
        # 窗口移动方向目标值单调变化，单调增或减

        sum = 0
        left = 0
        interval = len(nums) + 1
        for right, val in enumerate(nums):
            sum += val
            while sum >= s:
                interval = min(interval, right - left + 1)
                sum -= nums[left]
                left += 1
        return interval if interval <= len(nums) else 0



