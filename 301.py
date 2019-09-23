class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        st=[]
        for i in range(len(s)):
            if s[i]=='(':
                st.append()