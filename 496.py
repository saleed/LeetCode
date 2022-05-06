class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ndict={}
        st=[]
        for v in nums2:
            while len(st)>0 and v>st[-1]:
                ndict[st.pop()]=v
            st.append(v)
        for v in st:
            ndict[v]=-1
        res=[]
        for v in nums1:
            res.append(ndict[v])
        return res