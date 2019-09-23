import copy

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    i=len(nums)
    p=pow(2,i)
    cur=[]
    res=[]
    for i in range(p):
        cur=[]
        for id,j in enumerate(nums):
            if (i>>id)&1==1:
                cur.append(j)
        newcur=cur[:]
        res.append(newcur)
    return res


print subsets([1,2,3])