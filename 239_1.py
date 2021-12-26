class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        ##超时
        queue=[]
        res=[]
        for i in range(len(nums)):
            for j in range(len(queue)):
                if nums[i]>nums[queue[j]]:
                    queue=queue[:j]
                    break
            queue.append(i)
            if i<k-1:
                continue
            if i-queue[0]>k-1:
                queue=queue[1:]
            res.append(nums[queue[0]])
        return res

