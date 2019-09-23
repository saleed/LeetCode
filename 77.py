def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    vis=[0]*n
    res=[]
    cur=[]
    selectComb(vis,n,k,res,cur,1)
    return res


#77和77_2是两种思路
#77的想法是使用一个辅助的数组，记录哪个元素是否被访问过，如果被访问过，内层递归就不能再选，每层递归必会选出来一个数



#77_2则直接更暴力，直接遍历每个数，考虑当前遍历到的数是选还是不选，不选的话，组合的个数就是2^len(num)

def selectComb(vis,n,k,res,cur,sel):
    if k==0:
        newcur=cur[:]
        res.append(newcur)
    for i in range(sel,n+1):
        if vis[i-1]==0:
            vis[i-1]=1
            cur.append(i)
            selectComb(vis,n,k-1,res,cur,i)  ##sel为了避免重复 比如1，2，3，4，5如果第一个数字选择了2，那么剩下的只能从2后面的数选择，如果选择前面的，一定会重复，一位首位选1，然后选2这和首位选2，下一位选1是重复结果
            cur.pop()
            vis[i-1]=0
    return

print combine(4,2)
