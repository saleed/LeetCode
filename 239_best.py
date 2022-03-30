class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        arr=[]
        res=[]
        for i in range(len(nums)):

            for j in range(len(arr)):
                if nums[i]>nums[arr[j]]:
                    arr=arr[:j]
                    break
            arr.append(nums[i])
            if i<k:
                continue
            if i-arr[0]>k-1:
                arr=arr[1:]
            res.append(nums[arr[0]])
        return res


# s=Solution()
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# print(s.maxSlidingWindow(nums,k))
