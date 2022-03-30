class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        st = []
        lnum= 0
        rnum = 0
        for i in range(len(s)):
            if s[i] == '(':
                st.append('(')
            elif s[i]==')':
                if len(st) > 0:
                    st.pop()
                else:
                    rnum += 1

        lnum = len(st)

        res = []
        self.dfs(lnum, rnum, s, 0, "", res, [])
        return res

    def dfs(self, lnum, rnum, s, i, tmp, res, st):
        print(lnum,rnum,s,i,tmp,res,st)
        if i == len(s) and lnum == 0 and rnum == 0 and len(st) == 0:
            if tmp not in res:
                res.append(tmp[:])
            return
        if i < len(s) and rnum >= 0 and lnum >= 0:
            if s[i] == '(':
                if lnum > 0:
                    self.dfs(lnum - 1, rnum, s, i + 1, tmp, res, st)
                tmp += '('
                st.append('(')
                self.dfs(lnum, rnum, s, i + 1, tmp, res, st)
                st.pop()
                # tmp=tmp[:-1]
            elif s[i] == ')':
                if rnum > 0:
                    self.dfs(lnum, rnum - 1, s, i + 1, tmp, res, st)
                if len(st)>0:
                    tmp += ')'
                    st.pop()
                    self.dfs(lnum, rnum, s, i + 1, tmp, res, st)
                    st.append("(")
                    # tmp=tmp[:-1]
            else:
                tmp += s[i]
                self.dfs(lnum, rnum, s, i + 1, tmp, res, st)


s=Solution()
test=")(f"
print(s.removeInvalidParentheses(test))

