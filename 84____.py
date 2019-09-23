class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        st=[]
        for i in range(len(heights)):
            if len(st)==0:
                st.append(i)
