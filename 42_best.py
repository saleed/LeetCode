class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        que=[]
        res=0

        for i in range(len(height)):
            while len(que)>0 and height[que[-1]]<height[i]: ###
                width=(i - que[-1]) ####每个循环下计算的是当前柱子和左柱子，以及i之间围城的水量面积
                tmp=que.pop()
                if len(que)==0:
                    break
                minh=min(height[que[-1]],height[i])
                res+=(minh-height[tmp])*width
            que.append(i)
        return res
