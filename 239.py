import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        res = []
        que = collections.deque()
        for i in range(0, k):
            while len(que) > 0 and nums[que[-1]] < nums[i]:
                que.pop()
            que.append(i)
        res.append(nums[que[0]])

        for j in range(k, len(nums)):
            if que[0] == j - k:
                que.popleft()
            while len(que) > 0 and nums[que[-1]] < nums[j]:
                que.pop()
            que.append(j)
            res.append(nums[que[0]])
        return res


test = [1, 3, -1, -3, 5, 3, 6, 7]
a = Solution()
print(a.maxSlidingWindow(test, 3))

queue = collections.deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue[-1])
print(queue)

print(queue.popleft())
queue.append("Eric")
print(queue.pop())

print(queue)



