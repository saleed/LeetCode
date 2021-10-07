class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        for i in s:
            if i=="{" or i=="(" or i=="[":
                st.append(i)
            elif i=="}" and len(st)>0 and st[-1]=="{":
                st.pop()
            elif i == ")" and len(st) > 0 and st[-1] == "(":
                st.pop()
            elif i == "]" and len(st) > 0 and st[-1] == "[":
                st.pop()
            else:
                return False
        ###
        return len(st)==0 #注意这里很容易漏判
