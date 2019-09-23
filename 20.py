def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    st=[]
    for i in s:
        if i=='(' or i=='[' or i=='{':
            st.append(i)
        elif len(st)>0 and st[len(st)-1]=='(' and i==')':
            st.pop()
        elif len(st)>0 and st[len(st)-1] == '[' and i == ']':
            st.pop()
        elif len(st)>0 and st[len(st)-1] == '{' and i == '}':
            st.pop()
        else:
            return False
    if len(st)!=0:
        return False
    return True


test1="()[]{}"
print isValid(test1)

test2="([)]"
print isValid(test2)



test3=")"
print isValid(test3)

