#证明
#最初选择最外侧的两条边，每除去一条短边，往里选新边，相当于过滤了以短边为一侧的所有候选集合，

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p=0
        q=len(height)-1
        max_val=-float("inf")
        while p<q:
            max_val=max(max_val,(q-p)*min(height[p],height[q]))
            if height[p]<height[q]:
                p+=1
            else:
                q-=1
        return max_val