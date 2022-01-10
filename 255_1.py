class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """

        st=[]
        minv=-float("inf")
        for v in preorder:
            if v<minv:
                return False
            else:
                while len(st)>0 and st[-1]>v:
                    minv=st.pop()
                st.append(v)
        return True

