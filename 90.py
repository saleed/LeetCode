import copy

def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    dict={}
    for i in nums:
        if i in dict.keys():
            dict[i]+=1
        else:
            dict[i]=1
    res=[]
    rlt=[]
    for i in range(len(nums)+1):
        rlt=[]
        findSet(dict,i,[],rlt)
        newrlt=copy.deepcopy(rlt)
        res.extend(newrlt)
    return res



def findSet(dict,left,cur,rlt):
    print dict,left,cur,rlt
    if left==0:
        newcur=copy.deepcopy(cur)
        rlt.append(newcur)
        return
    for key,n in dict.items():
        keynum = dict[key]
        dict.pop(key)
        for j in range(0,keynum+1):
            if j<=left:
                cur.extend([key]*j)
                findSet(dict,left-j,cur,rlt)
                for t in range(j):
                    cur.pop()
        dict[key]=keynum#be careful for this

        break
    return


cur=[1,2,2,2]
print cur[:-3]
cur.extend([4,4])
print cur[:0]
for i in range(2):
    cur.pop()
print cur


a=[1,2,2]

print subsetsWithDup(a)

