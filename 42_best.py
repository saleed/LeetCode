class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        que=[]
        res=0

        for i in range(len(height)):
            while len(que)>0 and height[que[-1]]<height[i]:
                width=(i - que[-1])
                tmp=que.pop()
                if len(que)==0:
                    break
                minh=min(height[que[-1]],height[i])
                res+=(minh-height[tmp])*width
            que.append(i)
        return res
