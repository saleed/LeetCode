# coding:utf-8
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        ##思路是枚举高度，并维护一个单调栈

        st=[]
        p=0
        lbound=[0]*len(heights)
        rbound=[0]*len(heights)

        while p<len(heights):
            if len(st)>0:
                while len(st)>0:
                    if heights[st[-1]]<heights[p]:
                        break
                    st.pop()
            lbound[p] = heights[p] * (p-st[-1]) if len(st)>0 else heights[p]*(p+1)
            st.append(p)
            p+=1



        q=len(heights)-1
        st=[]
        while q>=0:
            if len(st)>0:
                while len(st) > 0:
                    if heights[st[-1]] < heights[q]:
                        break
                    st.pop()
            rbound[q] = heights[q] * (st[-1]-q) if len(st) > 0 else heights[q] * (len(heights)-q)
            st.append(q)
            q-=1
        maxv=-1
        print(lbound)
        print(rbound)
        for i in range(len(heights)):
            maxv=max(maxv,lbound[i]+rbound[i]-heights[i])
        return maxv


heights = [2,1,5,6,2,3]
a=Solution()
print(a.largestRectangleArea(heights))







