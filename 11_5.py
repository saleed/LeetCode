class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p=0
        q=len(height)-1
        maxarea=0
        while p<q:
            maxarea=max(maxarea,(q-p)*min(height[p],height[q]))
            if height[p]<height[q]:
                p+=1
            else:
                q-=1
        return maxarea
    ###假如height[p]==height[q] 选择一个p或q其中一个偏移，不会损失最大值，假设有比p，q更大的，一定不可能其中一条边是height[p]或者height[q]

