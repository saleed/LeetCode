def simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """




def fmtPath(path):
    i=0
    st=[]
    while i<len(path):
        while i<len(path) and path[i]=='/':
            i=i+1
        dot=""
        while i<len(path) and  path[i]=='.' :
            dot+='.'
            i=i+1
        if len(dot)>0:
            st.append(dot)
        arr=""
        while i<len(path) and path[i]>='a' and path[i]<='z':
            arr+=path[i]
            i=i+1
        if len(arr)>0:
            st.append(arr)
    # print st
    newst=[]
    for i in st:
        if i==".":
            continue
        elif i=="..":
            if len(newst)>0:
                newst.pop()
        else:
            newst.append(i)

    res="/"
    if len(newst)==0:
        return res

    for j in newst:
        res+=j
        res+='/'
    return res[:-1]









test="/home/"

# print fmtToList(test)
test="/a/./b/../../c/"

print(fmtPath(test))




test="/////"
print(test.split('/'))  #['', '', '', '', '', '']  结果为''