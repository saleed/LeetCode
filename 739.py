class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        st=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(st)==0 or temperatures[i]<=temperatures[st[-1]]:
                st.append(i)
                continue
            while len(st)>0 and temperatures[i]>temperatures[st[-1]]:
                res[st[-1]]=i-st[-1]
                st.pop()
            st.append(i)
        return res

