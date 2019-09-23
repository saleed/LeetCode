class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p=0
        q=len(height)-1
        maxarea=q*min(height[p],height[q])
        while p<q:
            maxarea=max(maxarea,(q-p)*min(height[p],height[q]))
            if height[p]<height[q]:
                p+=1
            else:
                q-=1
        return maxarea


##################假如边界上的两条边长度相同怎么办？？？？？？？？？？

