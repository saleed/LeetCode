class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        ##关键是如何证明通过这种方法找到的解是完备的
        p=0
        q=len(height)-1
        area=min(height[p],height[q])*(q-p)
        while p<q:
            if height[p]<height[q]:
                p+=1
            else:
                q+=1
            area=max(area,min(height[p],height[q]))
        return area

