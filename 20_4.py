class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        st=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                st.append(i)
            else:
                if len(st)==0:
                    return False
                top=st[-1]
                if (i==")" and top=="(") or (i=="}" and top=="{") or (i=="]" and top=="["):
                    st=st[:-1]
                    continue
                else:
                    return False

        return len(st)==0