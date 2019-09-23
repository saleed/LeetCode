import copy


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """



rlt=[]


# 递归思路：
# 统计左右括号的数目，最终目标是使左右括号都为N，
# 1.左括号没有达到N的时候一定可以添加左括号，如果当前右括号数目少于做左，也可以添加右括号
# 2.如果左括号达到N，只能添加右括号

def putblt(cur,n1,n2,n):
    # print cur ,n1,n2
    if n1==n2 and n1==n:
        rlt.append(cur)
        return
    if n1<n:
        newcur=copy.deepcopy(cur)
        newcur+="("
        putblt(newcur,n1+1,n2,n)
        if n2<n1:
            newcur = copy.deepcopy(cur)
            newcur+=")"
            putblt(newcur,n1,n2+1,n)
    else:
        cur+=")"
        putblt(cur,n1,n2+1,n)

    return

cur=""
putblt(cur,0,0,3)
print(rlt)




