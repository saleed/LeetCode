class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or len(nums) == 0:
            return 0
        # nums.sort()
        nums=self.radixSort(nums)
        print nums

        max = -float("inf")
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > max:
                max = nums[i] - nums[i - 1]
        return max


    ###how to right a radix sort with python
    def radixSort(self, A):
        for k in xrange(10):
            s = [[] for i in xrange(10)]
            for i in A:
                s[i / (10 ** k) % 10].append(i)
            # print s
            A = [a for b in s for a in b]
            print A
        return A


test=[100,3,2,1]
a=Solution()
print a.maximumGap(test)



