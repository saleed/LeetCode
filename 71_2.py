class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        phsplit=path.split('/')
        st=[]
        for part in phsplit:
            if part=='.' or part=='':
                continue
            elif part=='..':
                if len(st)>0:
                    st.pop()
            else:
                st.append(part)
        # print(phsplit)
        # print(st)
        # print(st[1])
        res=""
        if len(st)==0:
            return '/'
        i=0
        while st[i]=='..':
            i+=1
        for p in range(i,len(st)):
            res+="/"+st[p]

        return res


a=Solution()

t="/a/../../b/../c//.//"
print(a.simplifyPath(t))