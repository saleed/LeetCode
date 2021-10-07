class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        st=[]
        maxArea=0
        for i in range(len(height)):
            if len(st)==0 or height[st[-1]]>height[i]:
                st.append(i)
            else:
                sumArea=0
                while len(st)>0 and height[st[-1]]<=height[i]:
                    sumArea+=height[st[-1]]
                    st.pop()
                if len(st)>0:
                    maxArea+=min(height[i],height[st[-1]])*(i-st[-1]-1)-sumArea
                st.append(i)
            print(st,maxArea)
        return maxArea

if __name__=="__main__":
    a=Solution()
    test=[0,1,0,2,1,0,1,3,2,1,2,1]
    print(a.trap(test))




            